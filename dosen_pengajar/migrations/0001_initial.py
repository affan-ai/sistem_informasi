# Generated by Django 4.2.3 on 2023-09-01 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DosenPengajarModel',
            fields=[
                ('nrp', models.CharField(primary_key=True, serialize=False)),
                ('foto', models.ImageField(default='default.png', upload_to='uploads/profile/')),
                ('nama', models.CharField(max_length=100)),
                ('jk', models.CharField(choices=[('L', 'Laki-Laki'), ('P', 'Perempuan')], default='Laki-Laki', max_length=20)),
                ('tempat_lahir', models.CharField(max_length=100)),
                ('tanggal_lahir', models.DateField()),
                ('alamat', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=1000)),
                ('status', models.CharField(choices=[('Aktif', 'Aktif'), ('Tidak Aktif', 'Tidak Aktif')], default='A', max_length=100)),
                ('prodi', models.CharField(max_length=100)),
                ('agama', models.CharField(choices=[('Islam', 'Islam'), ('Kristen', 'Kristen'), ('Katolik', 'Katolik'), ('Hindu', 'Hindu'), ('Budha', 'Budha'), ('Konghucu', 'Konghucu')], default='Islam', max_length=50)),
            ],
        ),
    ]
