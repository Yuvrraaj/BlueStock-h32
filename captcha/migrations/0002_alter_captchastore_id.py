# Generated by Django 3.2.12 on 2022-03-06 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("captcha", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="captchastore",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
