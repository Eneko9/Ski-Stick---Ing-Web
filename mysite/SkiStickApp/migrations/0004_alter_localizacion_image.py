# Generated by Django 3.2.8 on 2021-12-17 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SkiStickApp', '0003_localizacion_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localizacion',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='SkiStickApp/static', verbose_name='Image'),
        ),
    ]
