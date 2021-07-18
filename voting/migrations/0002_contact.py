# Generated by Django 3.0.8 on 2020-09-05 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=50)),
                ('contact_phone', models.CharField(max_length=20)),
                ('contact_email', models.CharField(max_length=50)),
                ('contact_address', models.CharField(max_length=100)),
                ('contact_query', models.CharField(max_length=500)),
            ],
        ),
    ]