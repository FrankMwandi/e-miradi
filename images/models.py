from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250, blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    created = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                        related_name="images_created",
                        on_delete=models.CASCADE)
    user_likes = models.ManyToManyField(settings.AUTH_USER_MODEL,
                            related_name='images_liked',blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']
    
    def __str__(self):
        return self.title
