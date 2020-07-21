# Generated by Django 3.0.8 on 2020-07-20 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('concepts', '0002_auto_20200720_1450'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mappings', '0001_initial'),
        ('sources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapping',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='mappings_mapping_related_created_by', related_query_name='mappings_mappings_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mapping',
            name='from_concept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mappings_from', to='concepts.Concept'),
        ),
        migrations.AddField(
            model_name='mapping',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mappings_set', to='sources.Source'),
        ),
        migrations.AddField(
            model_name='mapping',
            name='sources',
            field=models.ManyToManyField(related_name='mappings', to='sources.Source'),
        ),
        migrations.AddField(
            model_name='mapping',
            name='to_concept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mappings_to', to='concepts.Concept'),
        ),
        migrations.AddField(
            model_name='mapping',
            name='to_source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mappings_to', to='sources.Source'),
        ),
        migrations.AddField(
            model_name='mapping',
            name='updated_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='mappings_mapping_related_updated_by', related_query_name='mappings_mappings_updated_by', to=settings.AUTH_USER_MODEL),
        ),
    ]