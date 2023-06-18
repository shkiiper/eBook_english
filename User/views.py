from django.contrib.auth import get_user_model, authenticate
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .models import Note, Dictionary, Level, TestType, Question, Testing, Review
from .serializers import UserSerializer, NoteSerializer, DictionarySerializer, LevelSerializer, TestTypeSerializer, \
    QuestionSerializer, TestingSerializer, TestingReadOnlySerializer, ReviewSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# Данный код представляет собой класс TokenObtainPairView, который является представлением (view) веб-приложения, написанного с использованием фреймворка Django
# и его модуля Django REST Framework. Давайте разберем его поэтапно:
# В начале класса определены разрешения (permissions) для доступа к данному представлению. В данном случае указано [AllowAny], что означает,
# что любой пользователь имеет право доступа к этому представлению.
# Метод get_extra_actions(self) возвращает пустой список дополнительных действий. В данном коде он не используется.
# Метод post(self, request) обрабатывает HTTP POST запросы, которые отправляются на данное представление. Он получает имя пользователя (username) и пароль (password) из данных запроса (request.data).
# Затем происходит аутентификация пользователя с помощью функции authenticate, которая проверяет предоставленные имя пользователя и пароль.
# Если пользователь существует и данные аутентификации верны, то выполняются следующие действия.
# Создается объект RefreshToken с использованием функции RefreshToken.for_user(user). Объект RefreshToken представляет токен обновления (refresh token), который может быть использован для получения нового доступного токена (access token).
# Значения access token и refresh token приводятся к строковому формату (str(refresh.access_token) и str(refresh)).
# Затем сериализуется объект пользователя (user) с использованием UserSerializer. Сериализация представляет процесс преобразования объекта Python в формат данных, который может быть легко передан через сеть или сохранен в базе данных.
# Данные пользователя полученные в результате сериализации (serializer.data) сохраняются в переменной user_data.
# Создается словарь response_data, содержащий значения access token, refresh token и данные пользователя.
# В случае успешной аутентификации, возвращается HTTP-ответ (Response) с данными response_data.
# Если аутентификация не прошла успешно (например, неверные учетные данные), возвращается HTTP-ответ с сообщением об ошибке ({'error': 'Invalid credentials'}) и статусом 400 (Bad Request).
# Этот код реализует точку входа API для получения пары токенов (access token и refresh token) в обмен на правильные учетные данные пользователя. Такой подход широко используется для аутентификации и авторизации пользователей в веб-приложениях.
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


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all() #queryset = Review.objects.all() определяет набор данных, из которого будут получены отзывы. В данном случае используется Review.objects.all(), что означает выбор всех объектов модели Review.
    serializer_class = ReviewSerializer #указывает на класс сериализатора, который будет использоваться для преобразования объектов Review в формат, подходящий для передачи по сети. ReviewSerializer должен быть определен в коде и содержать логику сериализации и десериализации объектов Review.
    permission_classes = [AllowAny] #определяет разрешения доступа к представлению. В данном случае используется [AllowAny], что позволяет любому пользователю иметь доступ к этому представлению без необходимости аутентификации или авторизации. Это может быть полезно, например, для предоставления публичного доступа к отзывам.


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

#это фильтрация для отображения определенных, выбранных вопросов, по фильтрам
    def get_queryset(self):
        level_id = self.request.query_params.get('level_id') # это строка означает что я проверяю наличие строки level_id, если есть то выполняется фильтрация по этому полю
        test_type_id = self.request.query_params.get('test_type_id')# это строка означает что я проверяю наличие строки test_type_id, если есть то выполняется фильтрация по этому полю

        if level_id and test_type_id:# если они есть (заданные параметры)
            queryset = Question.objects.filter(level_id=level_id, test_type_id=test_type_id) # фильтрация
        else: # если нет
            queryset = Question.objects.all() # достаю всех

        return queryset

    def get_serializer_class(self):#определяет класс сериализатора, который будет использоваться для преобразования объектов в формат, подходящий для передачи по сети.
        # В данном случае, если метод action представления (self.action) равен 'list' или 'retrieve', то возвращается класс QuestionSerializer, который будет использоваться для сериализации объектов модели Question.
        # В противном случае возвращается класс TestingSerializer, который будет использоваться для сериализации объектов модели Testing.
        if self.action == 'list' or self.action == 'retrieve':
            return QuestionSerializer
        return TestingSerializer


class UpdateUserAnswerAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, pk):
        try: #происходит попытка получить объект Question с помощью метода get() модели Question на основе указанного pk.
            question = Question.objects.get(id=pk)
        except Question.DoesNotExist:
            return Response({"error": "Question object not found"}, status=status.HTTP_404_NOT_FOUND)  # Если объект не найден, возвращается ответ с сообщением об ошибке и статусом 404 (Not Found).

        user_answer = request.data.get("user_answer")#Значение ответа пользователя (user_answer) извлекается из данных запроса (request.data.get("user_answer")).
        # Если значение не передано или равно None, возвращается ответ с сообщением об ошибке и статусом 400 (Bad Request).
        if user_answer is None:
            return Response({"error": "user_answer field is required"}, status=status.HTTP_400_BAD_REQUEST)

        question.user_answer = user_answer # Значение ответа пользователя (user_answer) присваивается атрибуту user_answer объекта question.

        if question.user_answer == question.correct_answer:#Проверяется, совпадает ли ответ пользователя с правильным ответом (question.correct_answer).
            # Если ответ правильный, устанавливается флаг is_correct в значение True, и к очкам пользователя (request.user.points) добавляется 4.

            question.is_correct = True
            request.user.points += 4
        else:
            question.is_correct = False  # В противном случае, флаг is_correct устанавливается в значение False.

        question.save()# Объект question сохраняется в базе данных методом save().


        #Объект Testing создается или получается существующий объект с помощью метода get_or_create().
        # Устанавливаются значения user, question, user_answer и is_correct для объекта testing.
        # Объект testing сохраняется в базе данных методом save().

        testing, created = Testing.objects.get_or_create(user=request.user, question=question)
        testing.user_answer = user_answer
        testing.is_correct = question.is_correct
        testing.save()

        serializer = QuestionSerializer(question) #Создается сериализатор QuestionSerializer с использованием объекта question.
        return Response(serializer.data) #Возвращается HTTP-ответ (Response) с данными сериализатора (serializer.data).
