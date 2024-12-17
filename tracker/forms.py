from django import forms
from datetime import datetime, timedelta
from .models import TimeEntry, Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', ]

class TimeEntryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            now = datetime.now()
             # Set initial values if not already provided
            self.fields['date'].initial = self.initial.get('date', now.date())
            self.fields['start_time'].initial = self.initial.get('start_time', now.time().replace(second=0, microsecond=0))
            self.fields['end_time'].initial = self.initial.get('end_time', (now + timedelta(hours=1)).time().replace(second=0, microsecond=0))
            print("Initial values:", {
                'date': self.fields['date'].initial,
                'start_time': self.fields['start_time'].initial,
                'end_time': self.fields['end_time'].initial
            })
    class Meta:
        model = TimeEntry
        fields = ['project', 'date', 'start_time', 'end_time']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'YYYY-MM-DD'
            }),
            'start_time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control',
                'placeholder': 'HH:MM'
            }),
            'end_time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control',
                'placeholder': 'HH:MM'
            }),
        }
        
