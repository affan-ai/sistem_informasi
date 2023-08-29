# Generated by Django 4.2.3 on 2023-08-27 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('nim', models.IntegerField(primary_key=True, serialize=False)),
                ('foto', models.ImageField(default='default.png', upload_to='uploads/profile/')),
                ('nama', models.CharField(max_length=100)),
                ('jk', models.CharField(choices=[('L', 'Laki-Laki'), ('P', 'Perempuan')], default='L', max_length=20)),
                ('tempat_lahir', models.CharField(max_length=100)),
                ('tanggal_lahir', models.DateField()),
                ('alamat', models.CharField(max_length=1000, null=True)),
                ('email', models.CharField(max_length=1000, null=True)),
                ('doswal', models.CharField(max_length=1000, null=True)),
                ('status', models.CharField(choices=[('Aktif', 'Aktif'), ('Tidak Aktif', 'Tidak Aktif')], default='Aktif', max_length=100)),
                ('angkatan', models.CharField()),
                ('semester', models.IntegerField()),
                ('agama', models.CharField(choices=[('Islam', 'Islam'), ('Kristen', 'Kristen'), ('Katolik', 'Katolik'), ('Hindu', 'Hindu'), ('Budha', 'Budha'), ('Konghucu', 'Konghucu')], default='Islam', max_length=50)),
                ('beasiswa', models.CharField(max_length=20)),
                ('jurusan', models.CharField(choices=[('Teknologi Informasi', 'Teknologi Informasi'), ('Akuntansi', 'Akuntansi'), ('Teknik Elektro', 'Teknik Elektro'), ('Mekatronika', 'Mekatronika')], default='Teknologi Informasi', max_length=50)),
            ],
        ),
    ]
