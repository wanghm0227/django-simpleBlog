# Generated by Django 3.2.5 on 2021-09-10 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0009_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
