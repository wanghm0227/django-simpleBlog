# Generated by Django 3.2.5 on 2021-09-09 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0004_auto_20210907_1647'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-post_time']},
        ),
    ]
