from django.contrib.auth import get_user_model
from django.db import models

from books.models import Books


class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    added_books = models.ManyToManyField(Books, related_name="obtained_books")

    class Meta:
        verbose_name_plural = "carts"

    @property
    def total_price(self):
        return sum(book.price for book in self.added_books.all())

    def remove_book(self, book_id):
        book = self.added_books.get(id=book_id)
        self.added_books.remove(book)