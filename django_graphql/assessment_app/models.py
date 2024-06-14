from django.db import models

# Create your models here.
class Task(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title