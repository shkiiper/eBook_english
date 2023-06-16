from django.urls import path, include
from rest_framework import routers
from .views import TestViewSet, AnswerStatisticViewSet, ScoreViewSet, TestTypeViewSet, DifficultyLevelViewSet, \
    QuestionViewSet

router = routers.DefaultRouter()
router.register(r'tests', TestViewSet, basename='test')
router.register(r'questions', QuestionViewSet, basename='question')
router.register('answer-statistics', AnswerStatisticViewSet, basename='answer-statistics')
router.register('scores', ScoreViewSet, basename='scores')
router.register('test-types', TestTypeViewSet, basename='test-types')
router.register('difficulty-levels', DifficultyLevelViewSet, basename='difficulty-levels')

urlpatterns = [
    path('', include(router.urls)),
]
