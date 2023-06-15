from django.contrib.auth import get_user_model, authenticate
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

from .models import Note, Dictionary
from .serializers import UserSerializer, NoteSerializer, DictionarySerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class TokenObtainPairView(APIView):
    permission_classes = [AllowAny]

    def get_extra_actions(self):
        return []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            serializer = UserSerializer(user)
            user_data = serializer.data

            response_data = {
                'access_token': access_token,
                'refresh_token': refresh_token,
                'user': user_data
            }
            return Response(response_data)
        else:
            return Response({'error': 'Invalid credentials'}, status=400)


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [AllowAny]


class DictionaryViewSet(viewsets.ModelViewSet):
    serializer_class = DictionarySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        return Dictionary.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)