# Generated by Django 2.1.5 on 2019-01-22 00:27

import django.db.models.expressions
from django.db import migrations

import metadeploy.api.models


class Migration(migrations.Migration):

    replaces = [
        ("api", "0041_auto_20190122_0018"),
        ("api", "0042_auto_20190122_0021"),
        ("api", "0043_auto_20190122_0022"),
        ("api", "0044_auto_20190122_0023"),
        ("api", "0045_auto_20190122_0025"),
    ]

    dependencies = [("api", "0040_auto_20190121_2345")]

    operations = [
        migrations.AlterModelOptions(
            name="step",
            options={
                "ordering": (
                    metadeploy.api.models.DottedArray(
                        django.db.models.expressions.F("step_num"), extra="."
                    ),
                )
            },
        )
    ]
