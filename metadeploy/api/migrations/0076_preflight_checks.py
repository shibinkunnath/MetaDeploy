# Generated by Django 2.2.2 on 2019-06-04 20:18

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("api", "0075_job_full_org_type")]

    operations = [
        migrations.RemoveField(model_name="plan", name="preflight_flow_name"),
        migrations.AddField(
            model_name="plan",
            name="preflight_checks",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True, default=list
            ),
        ),
    ]
