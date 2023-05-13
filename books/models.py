from django.db import models
from django.urls import reverse

# Create your models here.
class Books(models.Model):
    class Meta:
        app_label= 'books'
        verbose_name_plural = 'books'
    title = models.CharField(max_length = 200)
    description = models.TextField()
    author = models.CharField(max_length = 200)
    price = models.DecimalField(max_digits=5 , decimal_places=2)

    def __str__(self):
        return f'{self.author} : {self.title}'

    def get_absolute_url(self):
        return reverse('book_detail' , args=[self.id])
