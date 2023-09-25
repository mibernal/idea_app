from django.db import models

class Idea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='ideas/images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
