# Generated by Django 4.2.3 on 2023-09-01 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CutiModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(blank=True, max_length=100)),
                ('tanggal_mulai', models.DateField()),
                ('lama_cuti', models.CharField(max_length=100)),
                ('syarat_cuti', models.FileField(upload_to='uploads/cuti/')),
                ('keterangan', models.CharField(max_length=100)),
                ('status_cuti', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Disetujui', 'Disetujui'), ('Ditolak', 'Ditolak')], default='Pending', max_length=100)),
            ],
        ),
    ]
