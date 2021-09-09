# Generated by Django 3.2.5 on 2021-09-07 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0003_auto_20210906_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='coding', max_length=50),
        ),
    ]