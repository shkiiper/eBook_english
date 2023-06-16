from django.db import models

from User.models import User


class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    difficulty = models.ForeignKey(DifficultyLevel, on_delete=models.CASCADE)
    test_type = models.ForeignKey(TestType, on_delete=models.CASCADE)
    total_correct_answer = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=0)

    def __str__(self):
        return


class AnswerStatistic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.PositiveIntegerField(default=0)  # Результат в процентах (0-100)

    def __str__(self):
        return f"{self.user.username} - Result: {self.result}%"


class Score(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - Points: {self.points}"
