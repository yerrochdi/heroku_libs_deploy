# Generated by Django 2.1.3 on 2018-11-06 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ligne_Creesp_Lib',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lib_origine', models.CharField(max_length=200)),
                ('Lib_1', models.CharField(max_length=200)),
                ('Lib_2', models.CharField(max_length=200)),
                ('Lib_3', models.CharField(max_length=200)),
                ('Lib_4', models.CharField(max_length=200)),
                ('Lib_5', models.CharField(max_length=200)),
                ('Lib_6', models.CharField(max_length=200)),
                ('Lib_7', models.CharField(max_length=200)),
                ('Lib_8', models.CharField(max_length=200)),
                ('Lib_9', models.CharField(max_length=200)),
                ('Lib_10', models.CharField(max_length=200)),
                ('Lib_Choisi', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
