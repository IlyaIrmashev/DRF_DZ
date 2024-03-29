# Generated by Django 5.0.1 on 2024-01-17 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='courses/', verbose_name='картинка')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='lessons/', verbose_name='картинка')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('video', models.TextField(blank=True, null=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]
