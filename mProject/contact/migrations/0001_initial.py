# Generated by Django 4.2.1 on 2023-05-19 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cName', models.CharField(max_length=50)),
                ('cMail', models.EmailField(max_length=254)),
                ('cSub', models.CharField(max_length=200)),
                ('cSms', models.CharField(max_length=5000)),
            ],
        ),
    ]
