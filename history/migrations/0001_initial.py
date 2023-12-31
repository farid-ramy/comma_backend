# Generated by Django 4.2.7 on 2023-11-08 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0010_alter_user_address_alter_user_national_id_and_more'),
        ('branches', '0004_remove_branch_employee_id_workingin'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin_time', models.DateTimeField(auto_now_add=True)),
                ('checkout_time', models.DateTimeField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branches.branch')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkins', to='users.user')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkouts', to='users.user')),
            ],
        ),
    ]
