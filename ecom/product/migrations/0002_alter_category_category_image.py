# Generated by Django 3.2.14 on 2022-08-05 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(upload_to='categories'),
        ),
    ]