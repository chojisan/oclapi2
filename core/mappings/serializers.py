from rest_framework.fields import CharField, JSONField, IntegerField, SerializerMethodField
from rest_framework.serializers import ModelSerializer

from core.mappings.models import Mapping


class MappingListSerializer(ModelSerializer):
    id = CharField(source='versioned_object_id', read_only=True)
    source = CharField(source='parent_resource', read_only=True)
    owner = CharField(source='owner_name', read_only=True)
    update_comment = CharField(source='comment', required=False)
    url = CharField(source='version_url', read_only=True)
    version = CharField(read_only=True)
    to_concept_code = SerializerMethodField()
    to_concept_name = SerializerMethodField()

    class Meta:
        model = Mapping
        fields = (
            'external_id', 'retired', 'map_type', 'source', 'owner', 'owner_type',
            'from_concept_code', 'from_concept_name', 'from_concept_url',
            'to_concept_code', 'to_concept_name', 'to_concept_url',
            'from_source_owner', 'from_source_owner_type', 'from_source_url', 'from_source_name',
            'to_source_owner', 'to_source_owner_type', 'to_source_url', 'to_source_name',
            'url', 'version', 'id', 'versioned_object_id', 'versioned_object_url',
            'is_latest_version', 'update_comment', 'version_url'
        )

    @staticmethod
    def get_to_concept_code(obj):
        return obj.get_to_concept_code()

    @staticmethod
    def get_to_concept_name(obj):
        return obj.get_to_concept_name()


class MappingDetailSerializer(MappingListSerializer):
    type = CharField(source='resource_type', read_only=True)
    uuid = CharField(source='id', read_only=True)
    extras = JSONField(required=False)
    created_by = CharField(source='created_by.username', read_only=True)
    updated_by = CharField(source='created_by.username', read_only=True)
    parent_id = IntegerField(required=True)
    map_type = CharField(required=True)
    to_concept_url = CharField(required=True)
    from_concept_url = CharField(required=True)

    class Meta:
        model = Mapping
        fields = MappingListSerializer.Meta.fields + (
            'type', 'uuid', 'extras', 'created_at', 'updated_at',
            'created_by', 'updated_by', 'parent_id'
        )
        extra_kwargs = {'parent_id': {'write_only': True}}

    def create(self, validated_data):
        mapping = Mapping.persist_new(data=validated_data, user=self.context.get('request').user)
        self._errors.update(mapping.errors)
        return mapping

    def update(self, instance, validated_data):
        instance.extras = validated_data.get('extras', instance.extras)
        instance.external_id = validated_data.get('external_id', instance.external_id)
        instance.comment = validated_data.get('update_comment') or validated_data.get('comment')
        instance.retired = validated_data.get('retired', instance.retired)

        errors = Mapping.persist_clone(instance, self.context.get('request').user)
        if errors:
            self._errors.update(errors)
        return instance
