# Generated by Django 3.1.2 on 2020-10-15 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_id', models.IntegerField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
