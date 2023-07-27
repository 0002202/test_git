from django.db import models


# Create your models here.

class Question(models.Model):
    content = models.TextField(verbose_name="题目内容", primary_key=False, blank=False)
    answer = models.CharField(max_length=200, verbose_name="题目答案")
    difficulty = models.IntegerField(verbose_name="题目难度")
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    QUESTION_TYPE_CHOICES = (
        ('S', '单项选择'),
        ('M', '多项选择'),
        ('F', '填空'),
    )
    question_type = models.CharField(max_length=1, choices=QUESTION_TYPE_CHOICES, verbose_name="题目类型")

    def __str__(self):
        return self.content
