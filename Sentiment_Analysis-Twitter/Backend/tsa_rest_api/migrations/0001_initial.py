# Generated by Django 4.0.4 on 2022-04-30 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassifiedTweets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet', models.CharField(max_length=350)),
                ('sentiment', models.CharField(max_length=20)),
            ],
        ),
    ]
