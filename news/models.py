from django.db import models

# Create your models here.
from django.db import models

class News(models.Model):
    title_en = models.CharField(max_length=200)
    title_hi = models.CharField(max_length=200)
    title_fr = models.CharField(max_length=200)

    content_en = models.TextField()
    content_hi = models.TextField()
    content_fr = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_en