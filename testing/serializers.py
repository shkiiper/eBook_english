from rest_framework import serializers
from .models import Test, TestType, AnswerStatistic, Score, DifficultyLevel, Question


class AnswerStatisticSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    result = serializers.IntegerField()

    class Meta:
        model = AnswerStatistic
        fields = ['id', 'user', 'result']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'name', 'correct_answer', 'wrong_answer_1', 'wrong_answer_2', 'wrong_answer_3', 'input_result', 'result')


class TestTypeSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = TestType
        fields = ('id', 'name', 'difficulty', 'questions')

    def get_questions(self, obj):
        questions = obj.question_set.all()
        return QuestionSerializer(questions, many=True).data


class DifficultyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DifficultyLevel
        fields = ('id', 'name',)


class TestSerializer(serializers.ModelSerializer):
    difficulty = serializers.PrimaryKeyRelatedField(queryset=DifficultyLevel.objects.all())
    questions = QuestionSerializer(many=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Test
        fields = ['id', 'user', 'difficulty', 'test_type', 'total_correct_answer', 'total_questions', 'questions']


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('id', 'user', 'points',)
