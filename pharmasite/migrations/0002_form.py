# Generated by Django 3.1.2 on 2021-01-31 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmasite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=45)),
                ('Email', models.CharField(max_length=50)),
                ('Subject', models.CharField(max_length=45)),
                ('Message', models.CharField(max_length=30)),
            ],
        ),
    ]