# Generated by Django 4.2.3 on 2023-08-27 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DosenWaliModel',
            fields=[
                ('nrp', models.IntegerField(primary_key=True, serialize=False)),
                ('nama_doswal', models.CharField(max_length=100)),
                ('jk', models.CharField(choices=[('Laki-Laki', 'L'), ('Perempuan', 'P')], default='L', max_length=20)),
                ('prodi', models.CharField(max_length=100)),
                ('kelas', models.CharField(max_length=20)),
            ],
        ),
    ]
