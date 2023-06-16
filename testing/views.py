from requests import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from .models import Test, TestType, AnswerStatistic, Score, DifficultyLevel, Question
from .serializers import TestSerializer, TestTypeSerializer, AnswerStatisticSerializer, ScoreSerializer, \
    DifficultyLevelSerializer, QuestionSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [AllowAny]


class AnswerStatisticViewSet(viewsets.ModelViewSet):
    queryset = AnswerStatistic.objects.all()
    serializer_class = AnswerStatisticSerializer
    permission_classes = [AllowAny]


class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = [AllowAny]


class TestTypeViewSet(viewsets.ModelViewSet):
    queryset = TestType.objects.all()
    serializer_class = TestTypeSerializer
    permission_classes = [AllowAny]

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def check_user_answer(self, request, *args, **kwargs):
        question = self.get_object()
        user_answer = request.data.get('user_answer')

        is_correct = question.correct_choice == int(user_answer)

        if is_correct:
            question.is_correct = True
            question.save()

        data = {
            'question_id': question.id,
            'user_answer': user_answer,
            'is_correct': is_correct,
        }
        return Response(data)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class DifficultyLevelViewSet(viewsets.ModelViewSet):
    queryset = DifficultyLevel.objects.all()
    serializer_class = DifficultyLevelSerializer
    permission_classes = [AllowAny]
