from rest_framework import serializers
from django.contrib.auth import get_user_model

from User.models import Note, Dictionary, TestType, Question, Testing, Level, Review

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:#class Meta: - определяет класс Meta внутри сериализатора. В классе Meta определяются метаданные для сериализатора, включая модель, поля и дополнительные настройки.
        model = User #model = User - указывает модель, с которой будет связан сериализатор.
        fields = ('id', 'username', 'email', 'profile_photo', 'is_teacher', 'password', 'statistic', 'points')#определяет поля модели, которые будут включены в сериализацию и десериализацию.
        extra_kwargs = {'password': {'write_only': True}} #позволяет задать дополнительные настройки для определенных полей. Здесь указано, что поле password должно быть доступно только для записи (write-only) и не должно включаться в сериализованный вывод.

    def create(self, validated_data): #определяет метод create, который будет вызываться при создании нового объекта с использованием сериализатора.
        password = validated_data.pop('password') #получает значение поля
        user = User(**validated_data)#создает экземпляр модели User с использованием оставшихся проверенных данных
        user.set_password(password) #устанавливает хэшированный пароль для пользователя, используя метод set_password() модели пользователя Django. Пароль хэшируется для безопасного хранения в базе данных.
        user.save() #сохраняет
        return user


class NoteSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Note
        fields = '__all__'


class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = ('id', 'name', 'description', 'user')


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    user_username = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'review_text', 'user', 'user_username']


class TestTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestType
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class TestingReadOnlySerializer(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = Testing
        fields = '__all__'


class TestingSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = Testing
        fields = '__all__'
