from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class QuotesCreateView(LoginRequiredMixin, CreateView):
    model = Quote
    template_name = 'quote_new.html'
    fields = ('text', 'author', 'cover', 'source')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class QuotesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Quote
    template_name = 'quote_edit.html'
    fields = ('text', 'author', 'cover', 'source')
    login_url = 'login'

    def test_func(self):
        quote = self.get_object()
        return quote.user == self.request.user


class QuotesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Quote
    template_name = 'quote_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

    def test_func(self):
        quote = self.get_object()
        return quote.user == self.request.user

