from django.db import models

class Tasks(models.Model):
    class Meta:
        db_table = 'tasks'

    title = models.CharField(max_length=50)
    date_time = models.DateTimeField('date published')
    text = models.TextField(max_length=500)

