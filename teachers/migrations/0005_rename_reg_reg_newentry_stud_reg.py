# Generated by Django 5.1.3 on 2024-11-14 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_rename_reg_num_newentry_reg_reg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newentry',
            old_name='reg_reg',
            new_name='stud_reg',
        ),
    ]
