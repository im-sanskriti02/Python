# Generated by Django 3.1.3 on 2021-04-15 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20210415_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='typea',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.category'),
        ),
    ]
