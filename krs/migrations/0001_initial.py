# Generated by Django 4.2.3 on 2023-09-03 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mahasiswa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MataKuliah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=10)),
                ('nama', models.CharField(max_length=100)),
                ('jumlah_sks', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='KRS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mata_kuliah', models.CharField(max_length=200)),
                ('status', models.CharField(default='belum disetujui', max_length=20)),
                ('nilai', models.CharField(blank=True, max_length=20, null=True)),
                ('mahasiswa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mahasiswa.mahasiswa')),
            ],
        ),
    ]
