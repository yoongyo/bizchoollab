# Generated by Django 2.1 on 2020-02-05 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peed', '0003_auto_20200206_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peed',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='tag', to='peed.Tag'),
        ),
    ]