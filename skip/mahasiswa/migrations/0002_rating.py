# Generated by Django 2.2.1 on 2019-05-30 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mahasiswa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_1', models.IntegerField(default=0)),
                ('rate_2', models.IntegerField(default=0)),
                ('rate_3', models.IntegerField(default=0)),
                ('rate_4', models.IntegerField(default=0)),
                ('rate_5', models.IntegerField(default=0)),
                ('mahasiswa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mahasiswa.Mahasiswa')),
            ],
        ),
    ]
