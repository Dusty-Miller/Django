# Generated by Django 5.2.4 on 2025-07-31 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0002_post_uploaded_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="created",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="modified",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="uploaded_image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
