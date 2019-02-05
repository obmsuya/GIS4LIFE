from django.contrib import admin
from .models import  Quiz, TestGrades, ExamGrades

# Register your models here.


admin.site.register(Quiz)

admin.site.register(TestGrades)
admin.site.register(ExamGrades)