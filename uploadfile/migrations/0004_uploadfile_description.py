# Generated by Django 5.0.6 on 2024-07-09 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadfile', '0003_rename_file_path_uploadfile_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='description',
            field=models.TextField(default='Click the download bottom and download the question'),
        ),
    ]
