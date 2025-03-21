# Generated by Django 5.1.1 on 2024-10-24 21:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("workspace", "0002_alter_department_id_alter_workspace_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="department",
            name="workspace_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="departments",
                to="workspace.workspace",
            ),
        ),
    ]
