from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from .models import (
    Test, TestSession, Question, TestResponse, Answer, 
    Student, Instructor, VocabularyTerm, 
    ReadingPassage, PracticeExercise
)
# Register your models here.

class ReadingPassageAdmin(admin.ModelAdmin):
    formfield_overrides = {
        # models.CharField: {'widget': TextInput(attrs={'size':'2000'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
        models.CharField: {'widget': Textarea(attrs={'rows':20, 'cols':80})},
    }

    list_display = ['id',  'test', 'text',]
    list_filter = ['test']

    class Meta:
        model = ReadingPassage

admin.site.register(Test)
admin.site.register(TestSession)
# admin.site.register(SSAT)
admin.site.register(Question)
# admin.site.register(SSATMathQuestion)
admin.site.register(TestResponse)
admin.site.register(Answer)
# admin.site.register(Section)
admin.site.register(Student)
admin.site.register(Instructor)
# admin.site.register(TestSessionSection)
# admin.site.register(Assignment)
# admin.site.register(VocabularyRoot)
admin.site.register(VocabularyTerm)
# admin.site.register(VocabularyTermSynonym)
# admin.site.register(PracticeSetQuestion)
# admin.site.register(PracticeSet)
# admin.site.register(VocabularyCentralIdea)
admin.site.register(ReadingPassage, ReadingPassageAdmin)
admin.site.register(PracticeExercise)

