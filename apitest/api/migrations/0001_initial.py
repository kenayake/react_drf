# Generated by Django 4.2.7 on 2023-11-27 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prodi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodi', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nim', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='photo/')),
                ('prodi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.prodi')),
            ],
        ),
    ]