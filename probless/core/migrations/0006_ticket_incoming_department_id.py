# Generated by Django 5.1.1 on 2024-10-31 19:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_ticket_documentation'),
        ('workspace', '0003_alter_department_workspace_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='incoming_department_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='incoming_department', to='workspace.department'),
            preserve_default=False,
        ),
    ]
