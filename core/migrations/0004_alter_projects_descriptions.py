# Generated by Django 5.1.3 on 2024-12-02 17:00

import froala_editor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_technology_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='descriptions',
            field=froala_editor.fields.FroalaField(),
        ),
    ]
