from django.contrib import admin
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('email', 'feedback_text')
    search_fields = ('email', 'feedback_text')

admin.site.register(Feedback, FeedbackAdmin)