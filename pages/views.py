from django.shortcuts import render
from django.views.generic.base import TemplateView
from books.models import Books


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newest_books'] = Books.objects.order_by('-created_at')[:5]
        return context


def search_results(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Books.objects.filter(title__icontains=query)
    return render(request, 'pages/search_results.html', {'results': results, 'query': query})
