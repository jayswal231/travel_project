# Generated by Django 3.2.12 on 2023-05-25 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='packageenquiry',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
