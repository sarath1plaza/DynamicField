from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    subject = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name