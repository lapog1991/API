# Generated by Django 2.2.3 on 2019-07-12 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('std_id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('std_name', models.CharField(max_length=255)),
            ],
        ),
    ]