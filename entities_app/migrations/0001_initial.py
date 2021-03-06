# Generated by Django 3.2.4 on 2021-07-08 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entities',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Engagements',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('current_status', models.BooleanField(default=False)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities_app.entities', to_field='name')),
            ],
        ),
    ]
