# Generated by Django 3.2 on 2022-06-30 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='invalidatedaccesstoken',
            unique_together={('token',)},
        ),
        migrations.RemoveField(
            model_name='invalidatedaccesstoken',
            name='user',
        ),
    ]
