# Generated by Django 4.2.3 on 2023-09-03 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('krs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nilai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mata_kuliah', models.CharField(max_length=200, null=True)),
                ('nilai', models.CharField(max_length=50)),
                ('krs', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='nilai_rel', to='krs.krs')),
            ],
        ),
    ]
