from question_maker.models import Word, Definition
from rest_framework import serializers

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'word', 'similar_spellings', 'similar_sounds', 'theme_relations', 'associations']

class DefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Definition
        fields = '__all__'
