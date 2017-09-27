from django.contrib import admin

from .models import Question, Choice, Vote

class VoteInline(admin.StackedInline):
    model = Vote
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [VoteInline]

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
