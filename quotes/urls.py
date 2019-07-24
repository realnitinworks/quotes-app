from django.urls import path
from .views import QuotesListView, QuotesDetailView, QuotesCreateView, QuotesUpdateView, QuotesDeleteView

urlpatterns = [
    path("", QuotesListView.as_view(), name="home"),
    path("quote/<int:pk>/", QuotesDetailView.as_view(), name="quote_detail"),
    path("quote/new/", QuotesCreateView.as_view(), name="quote_new"),
    path("quote/<int:pk>/edit/", QuotesUpdateView.as_view(), name="quote_edit"),
    path("quote/<int:pk>/delete/", QuotesDeleteView.as_view(), name="quote_delete"),
]
