# Generated by Django 4.1.4 on 2023-02-08 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_post_image_name_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='first_name',
            new_name='user_name',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment_text',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='last_name',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
