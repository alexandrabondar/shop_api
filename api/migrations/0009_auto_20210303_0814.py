# Generated by Django 3.1.7 on 2021-03-03 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('authtoken', '0003_tokenproxy'),
        ('api', '0008_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='blablabla',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
