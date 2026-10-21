
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'subject',
            'description',
            'due_date',
            'priority',
            'status',
            'user',
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter task title',
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Enter subject',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe your task...',
                'rows': 4,
            }),
            'due_date': forms.DateInput(attrs={
                'type': 'date',
            }),
            'priority': forms.Select(),
            'status': forms.Select(),
        }
