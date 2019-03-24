from django.contrib import admin

from .models import Choice, Question

admin.site.site_header = 'Polls'
admin.site.index_title = 'Menu'


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']})
    ]
    inlines = [ChoiceInline]
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
