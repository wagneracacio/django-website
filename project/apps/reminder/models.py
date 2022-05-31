from django import forms
from django.db import models
from uuid import uuid4

class Lembrete(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100, null=True, blank=True)
    message = models.CharField(max_length=500, null=True, blank=True)

class LembreteForm(forms.ModelForm):
    class Meta:
        model = Lembrete
        fields = ['title', 'message']
        widgets = {'message': forms.Textarea()}
        