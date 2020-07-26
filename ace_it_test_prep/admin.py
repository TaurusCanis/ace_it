from django.contrib import admin
from .models import Test, TestSession, SSAT, Question, SSATMathQuestion, TestResponse, Answer, Section, TestSessionSection, Student, Instructor, Assignment

# Register your models here.

admin.site.register(Test)
admin.site.register(TestSession)
admin.site.register(SSAT)
admin.site.register(Question)
admin.site.register(SSATMathQuestion)
admin.site.register(TestResponse)
admin.site.register(Answer)
admin.site.register(Section)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(TestSessionSection)
admin.site.register(Assignment)
