from django.urls import path

from chapter2.books import BookListView

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
]