# Generated by Django 4.0.3 on 2022-06-08 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0003_answer_autor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='autor',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='autor',
            new_name='author',
        ),
    ]
