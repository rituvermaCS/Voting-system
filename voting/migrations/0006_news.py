# Generated by Django 3.0.8 on 2020-09-14 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0005_candidate'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_link', models.CharField(max_length=200)),
                ('news_text', models.CharField(max_length=1000)),
            ],
        ),
    ]
