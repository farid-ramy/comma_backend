# Generated by Django 4.2.6 on 2023-11-11 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_user_address_alter_user_national_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
    ]
