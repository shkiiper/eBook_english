from django.db import models
from User.models import User


class TestAlphabet(models.Model):
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    difficulty_level = models.ForeignKey('DifficultyLevel', on_delete=models.CASCADE)
    result = models.BooleanField(default=False)

    def __str__(self):
        return self.question


class TestNumbers(models.Model):
    name = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    difficulty_level = models.ForeignKey('DifficultyLevel', on_delete=models.CASCADE)
    result = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class TestFamilyFriends(models.Model):
    name = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    difficulty_level = models.ForeignKey('DifficultyLevel', on_delete=models.CASCADE)
    result = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class TestFoodDrinks(models.Model):
    name = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    difficulty_level = models.ForeignKey('DifficultyLevel', on_delete=models.CASCADE)
    result = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class DifficultyLevel(models.Model):
    level = models.CharField(max_length=100)

    def __str__(self):
        return self.level


class Statistics(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_completed_tests = models.IntegerField(default=0)
    total_correct_answers = models.IntegerField(default=0)

    def __str__(self):
        return f"Statistics for {self.user.username}"


class ExperiencePoints(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"Experience Points for {self.user.username}"


class CompletedTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_type = models.CharField(max_length=100)
    difficulty_level = models.ForeignKey(DifficultyLevel, on_delete=models.CASCADE)
    total_questions = models.IntegerField(default=0)
    total_correct_answers = models.IntegerField(default=0)
    completion_date = models.DateField(auto_now_add=True)
    test_alphabet = models.ForeignKey(TestAlphabet, null=True, blank=True, default=0, on_delete=models.CASCADE)
    test_numbers = models.ForeignKey(TestNumbers, null=True, blank=True, default=0, on_delete=models.CASCADE)
    test_family_friends = models.ForeignKey(TestFamilyFriends, null=True, blank=True, default=0,
                                            on_delete=models.CASCADE)
    test_food_drinks = models.ForeignKey(TestFoodDrinks, null=True, blank=True, default=0, on_delete=models.CASCADE)

    def __str__(self):
        return f"Completed Test - User: {self.user.username}, Type: {self.test_type}, Difficulty: {self.difficulty_level}"

    def save(self, *args, **kwargs):
        if self.total_correct_answers > self.total_questions:
            raise ValueError("The total number of correct answers cannot exceed the total number of questions.")

        super().save(*args, **kwargs)
