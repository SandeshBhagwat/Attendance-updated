# Generated by Django 3.1.3 on 2022-03-26 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20220323_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname1', models.TextField(max_length=50)),
                ('lastname1', models.TextField(max_length=50)),
                ('email1', models.EmailField(max_length=254)),
                ('message1', models.TextField(max_length=500)),
            ],
        ),
    ]
