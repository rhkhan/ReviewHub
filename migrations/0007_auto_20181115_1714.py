# Generated by Django 2.1.3 on 2018-11-15 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewhub', '0006_projectdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectdetails',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='project_description',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AddField(
            model_name='project',
            name='project_techs',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.DeleteModel(
            name='ProjectDetails',
        ),
    ]
