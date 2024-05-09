# Generated by Django 4.2 on 2023-04-29 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Universite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'Universite',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('universite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='Requetes.universite')),
            ],
            options={
                'db_table': 'Service',
            },
        ),
        migrations.CreateModel(
            name='Ecole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('universite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Requetes.universite')),
            ],
            options={
                'db_table': 'Ecole',
            },
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('ecole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Requetes.ecole')),
            ],
            options={
                'db_table': 'Departement',
            },
        ),
    ]