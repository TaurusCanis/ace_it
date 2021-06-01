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

    def get_field_names(self, excluded_field=None):
        return [field.name for field in Definition._meta.fields if getattr(self, field.name) != None and field.name != "examples" and field.name != excluded_field]


class Synonym(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    definition = models.ForeignKey(Definition, on_delete=models.CASCADE)
    has_been_vetted = models.BooleanField(default=False)
    difficulty = models.CharField(choices=[("E", "Easy"),("M", "Medium"),("H", "Hard")], max_length=1, default="M", null="True")

class SynonymAnswerOption(models.Model):
    synonym = models.ForeignKey(Synonym, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    value = models.CharField(max_length=200)
    answer_type = models.CharField(max_length=100, default="random_word")
    definition = models.ForeignKey(Definition, on_delete=models.CASCADE, default=None, blank=True, null=True)
    explanation = models.CharField(max_length=2500, blank=True, null=True)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in SynonymAnswerOption._meta.fields]

class Analogy(models.Model):
    pattern = models.CharField(choices=[("S", "Single"), ("D", "Double")], max_length=1)
    relationship = models.CharField(default="synonyms", max_length=50)
    word_A = models.ForeignKey(Definition, related_name="analogy_word_a_definition", on_delete=models.CASCADE)
    word_B = models.ForeignKey(Definition, related_name="analogy_word_b_definition", on_delete=models.CASCADE)
    word_C = models.ForeignKey(Definition, related_name="analogy_word_c_definition", on_delete=models.CASCADE, blank=True, null=True)
    has_been_vetted = models.BooleanField(default=False)
    difficulty = models.CharField(choices=[("E", "Easy"),("M", "Medium"),("H", "Hard")], max_length=1, default="M", null="True")

class AnalogyAnswerOption(models.Model):
    analogy = models.ForeignKey(Analogy, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    word_C = models.ForeignKey(Definition, related_name="analogy_answer_word_c_definition", on_delete=models.CASCADE, null=True, blank=True)
    word_D = models.ForeignKey(Definition, related_name="analogy_answer_word_d_definition", on_delete=models.CASCADE)
    explanation = models.CharField(max_length=2500, blank=True, null=True)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in AnalogyAnswerOption._meta.fields]
