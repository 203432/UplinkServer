# Generated by Django 4.2.2 on 2023-06-07 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_alter_post_published_alter_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateField(auto_now_add=True),
        ),
    ]
