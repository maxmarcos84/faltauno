# Generated by Django 5.0.4 on 2024-08-16 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_skillrating_current_average'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillrating',
            name='dislike_count',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='skillrating',
            name='like_count',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='skillrating',
            name='dislike',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='skillrating',
            name='like',
            field=models.BooleanField(default=True),
        ),
    ]
