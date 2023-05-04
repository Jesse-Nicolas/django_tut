from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # sorts and separates model fields on admin site as specified
    fieldsets = [
        (None, {'fields': ['text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # put choice creation onto the same admin page as question creation
    inlines = [ChoiceInline]
    # displays additional information about questions on the 'change question' admin page.
    list_display = ['text', 'pub_date', 'was_published_recently',]
    # this adds a filter option to the 'change quesiton' admin page. There are a handful of options for filtering the questions list based their pub_dates.
    list_filter = ['pub_date']
    search_fields = ['text']


admin.site.register(Question, QuestionAdmin)
