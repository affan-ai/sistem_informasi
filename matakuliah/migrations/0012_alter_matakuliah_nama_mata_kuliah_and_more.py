# Generated by Django 4.2.3 on 2023-08-29 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matakuliah', '0011_alter_matakuliah_nama_mata_kuliah'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matakuliah',
            name='nama_mata_kuliah',
            field=models.CharField(choices=[('Algoritma Pemrograman', 'Algoritma Pemrograman'), ('Struktur Data', 'Struktur Data'), ('Organisasi Arsitektur Komputer', 'Organisasi Arsitektur Komputer'), ('Desain Web', 'Desain Web'), ('Matematika Teknik', 'Matematika Teknik'), ('Sistem Informasi', 'Sistem Informasi')], max_length=100),
        ),
        migrations.AlterField(
            model_name='matakuliah',
            name='tipe',
            field=models.CharField(blank=True, choices=[('Praktikum', 'Praktikum'), ('Teori', 'Teori')], default='', max_length=100),
        ),
    ]
