from django.contrib.auth import get_user_model, authenticate
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

from .models import Note, Dictionary, Level, TestType, Question, Testing
from .serializers import UserSerializer, NoteSerializer, DictionarySerializer, LevelSerializer, TestTypeSerializer, \
    QuestionSerializer, TestingSerializer, TestingReadOnlySerializer

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
    queryset = Dictionary.objects.all()
    serializer_class = DictionarySerializer
    permission_classes = [AllowAny]


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [AllowAny]


class TestTypeViewSet(viewsets.ModelViewSet):
    queryset = TestType.objects.all()
    serializer_class = TestTypeSerializer
    permission_classes = [AllowAny]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]


class TestingViewSet(viewsets.ModelViewSet):
    queryset = Testing.objects.all()
    permission_classes = [AllowAny]

    def get_queryset(self):
        level_id = self.request.query_params.get('level_id')
        test_type_id = self.request.query_params.get('test_type_id')

        if level_id and test_type_id:
            queryset = Question.objects.filter(level_id=level_id, test_type_id=test_type_id)
        else:
            queryset = Question.objects.all()

        return queryset

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return QuestionSerializer
        return TestingSerializer


class UpdateUserAnswerAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, pk):
        try:
            question = Question.objects.get(id=pk)
        except Question.DoesNotExist:
            return Response({"error": "Question object not found"}, status=status.HTTP_404_NOT_FOUND)

        user_answer = request.data.get("user_answer")
        if user_answer is None:
            return Response({"error": "user_answer field is required"}, status=status.HTTP_400_BAD_REQUEST)

        question.user_answer = user_answer

        if question.user_answer == question.correct_answer:
            question.is_correct = True
            request.user.points += 4
        else:
            question.is_correct = False

        question.save()

        testing, created = Testing.objects.get_or_create(user=request.user, question=question)
        testing.user_answer = user_answer
        testing.is_correct = question.is_correct
        testing.save()

        total_questions = Testing.objects.filter(question=question).count()
        correct_answers = Testing.objects.filter(user=request.user, question=question, is_correct=True).count()
        filtered_questions = Testing.objects.filter(question=question, is_correct=True).count()

        request.user.statistic = (filtered_questions / total_questions) * 100

        request.user.save()

        serializer = QuestionSerializer(question)
        return Response(serializer.data)