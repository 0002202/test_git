# Generated by Django 4.2.3 on 2023-07-28 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testAPP', '0004_alter_question_difficulty'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
    ]