# Generated by Django 2.2.4 on 2019-10-08 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0020_remove_notice_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='files',
            field=models.FileField(blank=True, default='', null=True, upload_to='notice/files/'),
        ),
    ]
