# Generated by Django 2.2.7 on 2019-12-06 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epirecipe', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.TextField(max_length=100),
        ),
    ]