# Generated by Django 2.2 on 2019-07-01 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('institute', models.CharField(max_length=100)),
                ('designation', models.CharField(choices=[('prof', 'Professor'), ('masters', 'Masters Student'), ('phd', 'Research Students:Ph.D'), ('des', 'Dissertation Student'), ('alumni', 'Alumni')], max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
    ]
