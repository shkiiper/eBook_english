from rest_framework import serializers
from django.contrib.auth import get_user_model

from User.models import Note, Dictionary, TestType, Question, Testing, Level, Review

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'profile_photo', 'is_teacher', 'password', 'statistic', 'points')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'message', 'user')


class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = ('id', 'name', 'description', 'user')


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'review_text', 'user')


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
