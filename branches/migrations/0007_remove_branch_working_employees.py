# Generated by Django 4.2.6 on 2023-11-11 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0006_alter_branch_working_employees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='working_employees',
        ),
    ]
