# Generated by Django 4.2.3 on 2023-08-07 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('publish', 'Publish')], max_length=10),
        ),
    ]
