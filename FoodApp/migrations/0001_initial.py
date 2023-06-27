# Generated by Django 4.2.1 on 2023-06-22 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('carbs', models.FloatField()),
                ('protein', models.FloatField()),
                ('calories', models.FloatField()),
                ('calcium', models.FloatField()),
            ],
        ),
    ]
