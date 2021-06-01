from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

class Word(models.Model):
    word = models.CharField(max_length=250)
    similar_spellings = ArrayField(models.CharField(max_length=2500), null=True)
    similar_sounds = ArrayField(models.CharField(max_length=2500), null=True)
    theme_relations = ArrayField(models.CharField(max_length=2500), null=True)
    associations = ArrayField(models.CharField(max_length=2500), null=True)

    def haiku(self):
        return [f.name for f in Word._meta.get_fields()]

class Definition(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    definition = models.CharField(max_length=2500)
    partOfSpeech = models.CharField(max_length=15)
    synonyms = ArrayField(models.CharField(max_length=2500), null=True)
    antonyms = ArrayField(models.CharField(max_length=2500), null=True)
    entails = ArrayField(models.CharField(max_length=2500), null=True)
    also = ArrayField(models.CharField(max_length=2500), null=True)
    attribute = ArrayField(models.CharField(max_length=2500), null=True)
    similarTo = ArrayField(models.CharField(max_length=2500), null=True)
    typeOf = ArrayField(models.CharField(max_length=2500), null=True)
    hasTypes = ArrayField(models.CharField(max_length=2500), null=True)
    partOf = ArrayField(models.CharField(max_length=2500), null=True)
    hasParts = ArrayField(models.CharField(max_length=2500), null=True)
    isInstanceOf = ArrayField(models.CharField(max_length=2500), null=True)
    hasInstances = ArrayField(models.CharField(max_length=2500), null=True)
    memberOf = ArrayField(models.CharField(max_length=2500), null=True)
    hasMembers = ArrayField(models.CharField(max_length=2500), null=True)
    substanceOf = ArrayField(models.CharField(max_length=2500), null=True)
    hasSubstances = ArrayField(models.CharField(max_length=2500), null=True)
    inCategory = ArrayField(models.CharField(max_length=2500), null=True)
    hasCategories = ArrayField(models.CharField(max_length=2500), null=True)
    usageOf = ArrayField(models.CharField(max_length=2500), null=True)
    hasUsages = ArrayField(models.CharField(max_length=2500), null=True)
    inRegion = ArrayField(models.CharField(max_length=2500), null=True)
    regionOf = ArrayField(models.CharField(max_length=2500), null=True)
    pertainsTo = ArrayField(models.CharField(max_length=2500), null=True)
    examples = ArrayField(models.CharField(max_length=2500), null=True)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Definition._meta.fields if field.name != "word"]

class Synonym(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    definition = models.ForeignKey(Definition, on_delete=models.CASCADE)

class SynonymAnswerOption(models.Model):
    synonym = models.ForeignKey(Synonym, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    value = models.CharField(max_length=200)
    answer_type = models.CharField(max_length=100, default="random_word")
    has_been_vetted = models.BooleanField(default=False)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in SynonymAnswerOption._meta.fields]
