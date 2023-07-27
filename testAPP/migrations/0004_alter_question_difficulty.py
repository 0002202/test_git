# Generated by Django 4.2.3 on 2023-07-27 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testAPP', '0003_alter_question_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.CharField(choices=[('E', '简单'), ('M', '中等'), ('H', '困难')], max_length=1, verbose_name='题目难度'),
        ),
    ]