# Generated by Django 3.1.8 on 2021-04-14 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('concepts', '0008_auto_20210326_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='HierarchicalConcepts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_concept', to='concepts.concept')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_concept', to='concepts.concept')),
            ],
        ),
        migrations.AddField(
            model_name='concept',
            name='parent_concepts',
            field=models.ManyToManyField(through='concepts.HierarchicalConcepts', to='concepts.Concept'),
        ),
    ]