# Generated by Django 4.2.6 on 2023-11-08 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_user_address_alter_user_national_id_and_more'),
        ('branches', '0003_alter_branch_employee_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='employee_id',
        ),
        migrations.CreateModel(
            name='WorkingIN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='branches.branch')),
                ('employee_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]