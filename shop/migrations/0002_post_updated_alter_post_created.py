# Generated by Django 5.2.4 on 2025-07-31 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
