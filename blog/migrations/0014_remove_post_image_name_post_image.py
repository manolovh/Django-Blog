# Generated by Django 4.1.4 on 2023-02-08 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_comment_comment_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_name',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='posts'),
        ),
    ]
