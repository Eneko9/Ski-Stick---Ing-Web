# Generated by Django 3.2.8 on 2021-12-17 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SkiStickApp', '0007_opinion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='opinion',
            field=models.TextField(max_length=200),
        ),
    ]