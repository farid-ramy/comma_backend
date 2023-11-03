# Generated by Django 4.2.6 on 2023-10-23 20:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_created_at_user_modified_at_alter_user_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='national_id',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='Enter a valid national ID.', regex='^\\d{14}$')]),
        ),
    ]