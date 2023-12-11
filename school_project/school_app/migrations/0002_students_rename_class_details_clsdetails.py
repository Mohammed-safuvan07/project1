# Generated by Django 4.1.5 on 2023-12-11 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=25)),
                ('father_name', models.CharField(max_length=30)),
                ('phone_number', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='class_details',
            new_name='clsdetails',
        ),
    ]