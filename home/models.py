from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to='posts/',blank=False)

    def __str__(self):
        return self.title
