# Generated by Django 2.1.3 on 2018-11-12 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviewhub', '0002_freelancer'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('user_name', models.CharField(max_length=100)),
                ('user_password', models.CharField(max_length=50)),
                ('user_type', models.CharField(max_length=20)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviewhub.Country')),
            ],
        ),
    ]
