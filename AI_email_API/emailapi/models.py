from django.db import models

class EmailAnalysis(models.Model):
    text = models.TextField()
    summary = models.TextField(blank=True, null=True)
    sentiment = models.CharField(max_length=50, blank=True, null=True)
    urgency = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"EmailAnalysis #{self.id}"
