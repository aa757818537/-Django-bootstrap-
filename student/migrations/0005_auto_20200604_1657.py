# Generated by Django 2.1 on 2020-06-04 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20200604_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='level',
            field=models.CharField(choices=[('3', 'difficult'), ('1', 'easy'), ('2', 'general')], max_length=10, verbose_name='等级'),
        ),
    ]
