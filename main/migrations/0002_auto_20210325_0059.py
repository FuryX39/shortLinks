# Generated by Django 3.1.7 on 2021-03-24 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='short_id',
            field=models.CharField(blank=True, max_length=15, verbose_name='Short ID'),
        ),
    ]
