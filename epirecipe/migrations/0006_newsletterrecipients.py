# Generated by Django 2.2.7 on 2019-12-13 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epirecipe', '0005_food_favourite'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetterRecipients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]