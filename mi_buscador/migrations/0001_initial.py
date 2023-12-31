# Generated by Django 4.2.7 on 2023-11-28 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Palabra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('titulo', models.CharField(max_length=255)),
                ('relevancia', models.IntegerField()),
                ('palabra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mi_buscador.palabra')),
            ],
        ),
    ]
