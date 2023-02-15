# Generated by Django 4.1.3 on 2023-02-01 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mappings', '0035_remove_mapping_mappings_updated_4589ad_idx_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='mapping',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False), ('id', models.F('versioned_object_id'))), fields=['parent_id', 'is_active', 'retired', 'id', 'versioned_object_id'], name='mappings_all_for_count3'),
        ),
    ]