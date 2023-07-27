from django.db import models


# Create your models here.

class Question(models.Model):
    content = models.TextField(verbose_name="题目内容", primary_key=False, blank=False)
    answer = models.CharField(max_length=200, verbose_name="题目答案")
    DIFFICULTY_CHOICES = (
        ("E", '简单'),
        ("M", '中等'),
        ("H", '困难'),
    )
    difficulty = models.CharField(verbose_name="题目难度", max_length=1, choices=DIFFICULTY_CHOICES)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    QUESTION_TYPE_CHOICES = (
        ('S', '单项选择'),
        ('M', '多项选择'),
        ('F', '填空'),
    )
    question_type = models.CharField(max_length=1, choices=QUESTION_TYPE_CHOICES, verbose_name="题目类型")

    def __str__(self):
        return self.content

    # 钩子函数，将返回choices定义的数据
    def get_question_type_display(self):
        return dict(self.QUESTION_TYPE_CHOICES)[self.question_type]

    def get_difficulty_display(self):
        return dict(self.DIFFICULTY_CHOICES)[self.difficulty]
