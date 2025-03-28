# Generated by Django 5.1.1 on 2024-11-04 23:45

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_alter_ticket_incoming_department_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="documentation",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True,
                help_text="Documentation on how the ticket was solved",
                null=True,
            ),
        ),
    ]
