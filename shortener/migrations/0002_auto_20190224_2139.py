# Generated by Django 2.1.7 on 2019-02-24 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='full_url',
            field=models.URLField(max_length=800, unique=True),
        ),
    ]