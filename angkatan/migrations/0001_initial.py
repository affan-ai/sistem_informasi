# Generated by Django 4.2.3 on 2023-08-27 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Angkatan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nama_angkatan', models.IntegerField()),
                ('kurikulum', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
