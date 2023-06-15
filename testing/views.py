from django.db.models import Q
from requests import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from .models import TestAlphabet, TestNumbers, TestFamilyFriends, TestFoodDrinks, Statistics, ExperiencePoints, \
    CompletedTest, DifficultyLevel
from .serializers import (
    TestAlphabetSerializer,
    TestNumbersSerializer,
    TestFamilyFriendsSerializer,
    TestFoodDrinksSerializer,
    StatisticsSerializer,
    ExperiencePointsSerializer, CompletedTestSerializer, DifficultyLevelSerializer,
)


class TestAlphabetViewSet(viewsets.ModelViewSet):
    queryset = TestAlphabet.objects.all()
    serializer_class = TestAlphabetSerializer

    @action(detail=True, methods=['post'])
    def set_answer_result(self, request, pk=None):
        test_alphabet = self.get_object()
        answer = request.data.get('answer')

        if answer == test_alphabet.answer:
            test_alphabet.result = True
        else:
            test_alphabet.result = False

        test_alphabet.save()

        serializer = self.get_serializer(test_alphabet)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def set_option_result(self, request, pk=None):
        test_alphabet = self.get_object()
        option = request.data.get('option')

        if option != test_alphabet.answer:
            test_alphabet.result = False
            test_alphabet.save()

        serializer = self.get_serializer(test_alphabet)
        return Response(serializer.data)


class TestNumbersViewSet(viewsets.ModelViewSet):
    queryset = TestNumbers.objects.all()
    serializer_class = TestNumbersSerializer

    @action(detail=True, methods=['post'])
    def set_answer_result(self, request, pk=None):
        test_numbers = self.get_object()
        answer = request.data.get('answer')

        if answer == test_numbers.answer:
            test_numbers.result = True
        else:
            test_numbers.result = False

        test_numbers.save()

        serializer = self.get_serializer(test_numbers)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def set_option_result(self, request, pk=None):
        test_numbers = self.get_object()
        option = request.data.get('option')

        if option != test_numbers.answer:
            test_numbers.result = False
            test_numbers.save()

        serializer = self.get_serializer(test_numbers)
        return Response(serializer.data)


class TestFamilyFriendsViewSet(viewsets.ModelViewSet):
    queryset = TestFamilyFriends.objects.all()
    serializer_class = TestFamilyFriendsSerializer

    @action(detail=True, methods=['post'])
    def set_answer_result(self, request, pk=None):
        test_family_friends = self.get_object()
        answer = request.data.get('answer')

        if answer == test_family_friends.answer:
            test_family_friends.result = True
        else:
            test_family_friends.result = False

        test_family_friends.save()

        serializer = self.get_serializer(test_family_friends)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def set_option_result(self, request, pk=None):
        test_family_friends = self.get_object()
        option = request.data.get('option')

        if option != test_family_friends.answer:
            test_family_friends.result = False
            test_family_friends.save()

        serializer = self.get_serializer(test_family_friends)
        return Response(serializer.data)


class TestFoodDrinksViewSet(viewsets.ModelViewSet):
    queryset = TestFoodDrinks.objects.all()
    serializer_class = TestFoodDrinksSerializer

    @action(detail=True, methods=['post'])
    def set_answer_result(self, request, pk=None):
        test_food_drinks = self.get_object()
        answer = request.data.get('answer')

        if answer == test_food_drinks.answer:
            test_food_drinks.result = True
        else:
            test_food_drinks.result = False

        test_food_drinks.save()

        serializer = self.get_serializer(test_food_drinks)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def set_option_result(self, request, pk=None):
        test_food_drinks = self.get_object()
        option = request.data.get('option')

        if option != test_food_drinks.answer:
            test_food_drinks.result = False
            test_food_drinks.save()

        serializer = self.get_serializer(test_food_drinks)
        return Response(serializer.data)


class DifficultyLevelViewSet(viewsets.ModelViewSet):
    queryset = DifficultyLevel.objects.all()
    serializer_class = DifficultyLevelSerializer
    permission_classes = [AllowAny]


class StatisticsViewSet(viewsets.ModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer
    permission_classes = [AllowAny]


class ExperiencePointsViewSet(viewsets.ModelViewSet):
    queryset = ExperiencePoints.objects.all()
    serializer_class = ExperiencePointsSerializer
    permission_classes = [AllowAny]


class CompletedTestViewSet(viewsets.ModelViewSet):
    queryset = CompletedTest.objects.all()
    serializer_class = CompletedTestSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        completed_test = serializer.save()

        self.update_statistics(completed_test)

        self.update_experience_points(completed_test)

        return completed_test

    @staticmethod
    def update_statistics(completed_test):
        user = completed_test.user
        total_correct_answers = completed_test.total_correct_answers

        try:
            statistics = Statistics.objects.get(user=user)
        except Statistics.DoesNotExist:
            statistics = Statistics.objects.create(user=user)

        statistics.total_completed_tests += 1
        statistics.total_correct_answers += total_correct_answers
        statistics.success_percentage = (statistics.total_correct_answers / (
                statistics.total_completed_tests * completed_test.total_questions)) * 100
        statistics.save()

    @staticmethod
    def update_experience_points(completed_test):
        user = completed_test.user
        total_correct_answers = completed_test.total_correct_answers

        try:
            experience_points = ExperiencePoints.objects.get(user=user)
        except ExperiencePoints.DoesNotExist:
            experience_points = ExperiencePoints.objects.create(user=user)

        experience_points.points += total_correct_answers * 4
        experience_points.save()

