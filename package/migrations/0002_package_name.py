# Generated by Django 3.2.12 on 2023-05-25 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='name',
            field=models.CharField(default=1, max_length=299),
            preserve_default=False,
        ),
    ]