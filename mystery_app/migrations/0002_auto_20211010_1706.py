# Generated by Django 3.0.1 on 2021-10-10 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystery_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution', models.CharField(max_length=30)),
                ('hint_1', models.CharField(max_length=30)),
                ('hint_2', models.CharField(max_length=30)),
                ('hint_3', models.CharField(max_length=30)),
                ('hint_4', models.CharField(max_length=30)),
                ('hint_5', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Guess',
        ),
    ]
