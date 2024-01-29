# Generated by Django 5.0.1 on 2024-01-29 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_buyer_lesson_buyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='оплачено'),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_intent_id',
            field=models.CharField(default='NULL', max_length=100, verbose_name='id_платежа'),
        ),
    ]
