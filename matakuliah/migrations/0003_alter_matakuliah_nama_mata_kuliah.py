# Generated by Django 4.2.3 on 2023-09-02 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matakuliah', '0002_alter_matakuliah_nama_mata_kuliah'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matakuliah',
            name='nama_mata_kuliah',
            field=models.CharField(choices=[('Struktur Data', 'Struktur Data'), ('Algoritma Pemrograman', 'Algoritma Pemrograman'), ('Sistem Informasi', 'Sistem Informasi'), ('Matematika Teknik', 'Matematika Teknik'), ('Organisasi Arsitektur Komputer', 'Organisasi Arsitektur Komputer'), ('Desain Web', 'Desain Web')], max_length=100),
        ),
    ]
