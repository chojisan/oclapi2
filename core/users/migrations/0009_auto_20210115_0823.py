# Generated by Django 3.0.9 on 2021-01-15 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_delete_pinneditem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='uri',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
    ]