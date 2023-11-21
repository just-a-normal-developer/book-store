from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from books.models import Books


class HomePageView(TemplateView):
    template_name = "home.html"


class FeaturedContentView(TemplateView):
    template_name = "featured_content.html"


class RecentUpdatesView(TemplateView):
    template_name = "recent_updates.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        new_books = Books.objects.order_by("-created_at")[:5]
        if new_books.count() < 5:
            remaining_books = Books.objects.exclude(
                pk__in=[book.pk for book in new_books]
            ).order_by("-created_at")[: 5 - new_books.count()]
            new_books = list(new_books) + list(remaining_books)

        context["new_books"] = new_books
