# Generated by Django 3.1.7 on 2021-03-03 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210303_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='blablabla',
            field=models.CharField(default='3', max_length=20),
        ),
    ]