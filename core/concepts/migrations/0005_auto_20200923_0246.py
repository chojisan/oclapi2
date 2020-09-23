# Generated by Django 3.0.9 on 2020-09-23 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0006_auto_20200729_0718'),
        ('concepts', '0004_auto_20200722_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concept',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='concepts_set', to='sources.Source'),
        ),
    ]