# Generated by Django 4.2.5 on 2023-09-23 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_alter_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_checked_by_admin',
            field=models.BooleanField(default=False),
        ),
    ]