# Generated by Django 4.1.4 on 2023-02-03 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_author_email_alter_post_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='capiton',
            field=models.CharField(max_length=20),
        ),
    ]
