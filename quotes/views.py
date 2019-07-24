from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Quote


class QuotesListView(ListView):
    model = Quote
    template_name = 'home.html'
    context_object_name = 'quotes'


class QuotesDetailView(DetailView):
    model = Quote
    template_name = 'quote_detail.html'
    context_object_name = 'quote'


class QuotesCreateView(CreateView):
    model = Quote
    template_name = 'quote_new.html'
    fields = ('text', 'author', 'cover', 'source')


class QuotesUpdateView(UpdateView):
    model = Quote
    template_name = 'quote_edit.html'
    fields = ('text', 'author', 'cover', 'source')


class QuotesDeleteView(DeleteView):
    model = Quote
    template_name = 'quote_delete.html'
    success_url = reverse_lazy('home')
