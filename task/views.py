from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Classed-Based View
from django.views.generic import TemplateView
from django.views.generic import ListView

from .models import Category
from .tests.factories import CategoryFactory

def home_page(request):
    date = datetime(2000, 1, 1)
    return render(request, 'task/home.html', {'date': date})

class HomePageView(TemplateView):
    template_name = 'task/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date'] = datetime(2018, 6, 6)
        return context

class CategoryListView(ListView):
    model = Category
    category = CategoryFactory()

class TodoView(TemplateView):
    template_name = 'task/todo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = (
            Category.objects
            .all()
            .prefetch_related('todoentry_set')
        )
        return context
