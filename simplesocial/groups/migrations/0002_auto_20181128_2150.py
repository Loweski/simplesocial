# Generated by Django 2.0.5 on 2018-11-29 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmember',
            name='group',
            field=models.ForeignKey(on_delete='cascade', related_name='memberships', to='groups.Group'),
        ),
    ]
