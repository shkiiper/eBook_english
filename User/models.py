from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    statistic = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_user_set',
        related_query_name='custom_user'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set',
        related_query_name='custom_user'
    )

    def __str__(self):
        return self.username


class Note(models.Model):
    message = models.TextField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.message


class Review(models.Model):
    review_text = models.TextField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.review_text


class Dictionary(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=50, default='Unknown')

    def __str__(self):
        return self.name


class TestType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    choice1 = models.CharField(max_length=200, default='вариант')
    choice2 = models.CharField(max_length=200, default='вариант')
    choice3 = models.CharField(max_length=200, default='вариант')
    correct_answer = models.CharField(max_length=200)
    user_answer = models.CharField(max_length=200, null=True, blank=True)
    is_correct = models.BooleanField(default=False)
    test_type = models.ForeignKey(TestType, on_delete=models.CASCADE, default='')
    level = models.ForeignKey(Level, on_delete=models.CASCADE, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.question_text


class Testing(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    user_answer = models.CharField(max_length=200, null=True, blank=True)
    is_correct = models.BooleanField(default=False)
    total_questions = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    statistic = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.total_questions = Testing.objects.filter(user=self.user).count()
        self.correct_answers = Testing.objects.filter(user=self.user, is_correct=1).count()
        self.user.statistic = (self.correct_answers / self.total_questions) * 100
        self.user.save()

        super(Testing, self).save(*args, **kwargs)