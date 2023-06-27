# Generated by Django 4.2.2 on 2023-06-27 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_teacher_options_alter_teacher_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='second_name',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone_number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
