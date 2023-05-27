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
    cover = models.ImageField(upload_to = 'BookCover', blank = True)

    def __str__(self):
        return f'{self.author} : {self.title}'

    def get_absolute_url(self):
        return reverse('book_detail' , args=[self.id])

class Comments(models.Model):
    user = models
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add = True)