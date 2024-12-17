from django.contrib.auth.models import User
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class TimeEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def duration(self):
        from datetime import datetime, timedelta
        start = datetime.combine(self.date, self.start_time)
        
        # If end_time is earlier than start_time, assume it is the next day
        end_date = self.date if self.end_time >= self.start_time else self.date + timedelta(days=1)
        end = datetime.combine(end_date, self.end_time)
        
        return round((end - start).total_seconds() / 3600, 2)  # Returns duration in hours
        '''
            How it Works
            Standard Cases:

            If end_time is later than or equal to start_time, both start and end are on the same day.
            Cross-Date Cases:

            If end_time is earlier than start_time (e.g., shift starts at 8 PM and ends at 4 AM), the end_date is incremented by one day (date + timedelta(days=1)).
            Duration Calculation:

            The difference between start and end is calculated and converted from seconds to hours.
        '''

    def __str__(self):
        return f"{self.user.username} - {self.project.name} ({self.date})"
