# Generated by Django 4.2.3 on 2023-08-29 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matakuliah', '0014_alter_matakuliah_nama_mata_kuliah'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matakuliah',
            name='nama_mata_kuliah',
            field=models.CharField(choices=[('Matematika Teknik', 'Matematika Teknik'), ('Algoritma Pemrograman', 'Algoritma Pemrograman'), ('Sistem Informasi', 'Sistem Informasi'), ('Struktur Data', 'Struktur Data'), ('Organisasi Arsitektur Komputer', 'Organisasi Arsitektur Komputer'), ('Desain Web', 'Desain Web')], max_length=100),
        ),
    ]
