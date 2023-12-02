# Generated by Django 4.2.6 on 2023-12-01 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('branches', '0007_remove_branch_working_employees'),
        ('packages', '0005_package_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='package',
            unique_together={('branch', 'name')},
        ),
        migrations.CreateModel(
            name='PackageAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(max_length=50)),
                ('attribute_value', models.CharField(max_length=225)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='packages.package')),
            ],
        ),
    ]
