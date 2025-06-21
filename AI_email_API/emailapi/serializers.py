from rest_framework import serializers
from .models import EmailAnalysis

class EmailAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailAnalysis
        fields = ['id', 'text', 'summary', 'sentiment', 'urgency', 'created_at']
        read_only_fields = ['summary', 'sentiment', 'urgency', 'created_at']
