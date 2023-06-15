from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    TestAlphabetViewSet,
    TestNumbersViewSet,
    TestFamilyFriendsViewSet,
    TestFoodDrinksViewSet,
    StatisticsViewSet,
    ExperiencePointsViewSet, DifficultyLevelViewSet,
)

router = DefaultRouter()
router.register(r'test_alphabet', TestAlphabetViewSet, basename='test_alphabet')
router.register(r'test_numbers', TestNumbersViewSet, basename='test_numbers')
router.register(r'test_family_friends', TestFamilyFriendsViewSet, basename='test_family_friends')
router.register(r'test_food_drinks', TestFoodDrinksViewSet, basename='test_food_drinks')
router.register(r'difficulty-levels', DifficultyLevelViewSet,  basename='difficulty_levels')
router.register(r'statistics', StatisticsViewSet, basename='statistics')
router.register(r'experience_points', ExperiencePointsViewSet, basename='experience_points')

urlpatterns = [
    path('', include(router.urls)),
]
