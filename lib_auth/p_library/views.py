# from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from p_library.models import Book, Publisher, Reader
from .forms import BookForm


class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('p_library:book_list')
    template_name = 'book_edit.html'


class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    success_url = reverse_lazy('p_library:book_list')
    fields = ['title', 'cover', 'price', 'copy_count']
    template_name = 'book_edit.html'


class BookRead(ListView):
    model = Book
    template_name = 'book_list.html'
    

def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    books_count = books.count()
    user = request.user
    biblio_data = {
        "title": "мою библиотеку",
        "books_count": books_count,
        "books": books,
        "user": user,
    }
    return HttpResponse(template.render(biblio_data))

def pub_list(request):
    template = loader.get_template('publishers.html')
    publishers = Publisher.objects.all()
    books = Book.objects.all()
    user = request.user
    pub_data = {
        "publishers": publishers,
        "books": books,
        "user": user,
    }
    return HttpResponse(template.render(pub_data))

def reader_list(request):
    template = loader.get_template('readers.html')
    readers = Reader.objects.all()
    books = Book.objects.all()
    user = request.user
    read_data = {
        "readers": readers,
        "books": books,
        "user": user,
    }
    return HttpResponse(template.render(read_data))
