# Generated by Django 2.1.3 on 2018-11-14 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewhub', '0004_auto_20181114_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='completion_date',
            field=models.DateField(),
        ),
    ]