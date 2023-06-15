from django.db.models import Sum
from rest_framework import serializers
from .models import TestAlphabet, TestNumbers, TestFamilyFriends, TestFoodDrinks, Statistics, ExperiencePoints, \
    CompletedTest, DifficultyLevel


class TestAlphabetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestAlphabet
        fields = '__all__'


class TestNumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestNumbers
        fields = '__all__'


class TestFamilyFriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestFamilyFriends
        fields = '__all__'


class TestFoodDrinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestFoodDrinks
        fields = '__all__'


class DifficultyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DifficultyLevel
        fields = ['id', 'level']


class StatisticsSerializer(serializers.ModelSerializer):
    success_percentage = serializers.SerializerMethodField()

    def get_success_percentage(self, obj):
        completed_tests = CompletedTest.objects.filter(user=obj.User)
        total_completed_tests = completed_tests.count()
        total_correct_answers = completed_tests.aggregate(Sum('total_correct_answers'))['total_correct_answers__sum']

        if total_completed_tests and total_correct_answers is not None:
            total_questions = completed_tests.first().total_questions
            return (total_correct_answers / (total_completed_tests * total_questions)) * 100
        else:
            return 0

    class Meta:
        model = Statistics
        fields = ['id', 'success_percentage']


class ExperiencePointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperiencePoints
        fields = '__all__'


class CompletedTestSerializer(serializers.ModelSerializer):
    test_alphabet = TestAlphabetSerializer()
    test_numbers = TestNumbersSerializer()
    test_family_friends = TestFamilyFriendsSerializer()
    test_food_drinks = TestFoodDrinksSerializer()

    class Meta:
        model = CompletedTest
        fields = '__all__'

