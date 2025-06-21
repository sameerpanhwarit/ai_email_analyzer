from django.contrib import admin
from .models import EmailAnalysis

@admin.register(EmailAnalysis)
class EmailAnalysisAdmin(admin.ModelAdmin):
    list_display = ('id', 'sentiment', 'urgency', 'created_at')
    list_filter = ('sentiment', 'urgency', 'created_at')
    search_fields = ('text', 'summary')