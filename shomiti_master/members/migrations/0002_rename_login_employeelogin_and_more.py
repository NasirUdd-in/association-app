# Generated by Django 4.2.3 on 2023-08-01 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Login",
            new_name="EmployeeLogin",
        ),
        migrations.RenameField(
            model_name="employee",
            old_name="did_number",
            new_name="nid_number",
        ),
    ]