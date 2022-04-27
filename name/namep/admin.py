from dataclasses import fields
from django.contrib import admin

from namep.models import Question
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fields =['text']

admin.site.register(Question)
