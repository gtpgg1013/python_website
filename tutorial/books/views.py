from django.shortcuts import render, redirect
from django.views import generic
from django.utils import timezone
from django.urls import reverse
from books.models import Author, Book, Publisher

class BooksModelView(generic.TemplateView):
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Book', 'Author', 'Publisher']
        return context

class MakeRecordView(generic.TemplateView):
    template_name = 'books/make_record.html'

class BookList(generic.ListView):
    model = Book

class AuthorList(generic.ListView):
    model = Author

class PublisherList(generic.ListView):
    model = Publisher

class BookDetail(generic.DetailView):
    model = Book

class AuthorDetail(generic.DetailView):
    model = Author

class PublisherDetail(generic.DetailView):
    model = Publisher

def make_record(request):
    if request.method == 'POST':
        book = Book()
        book.publication_field = timezone.now()

        author = Author()
        publisher = Publisher()
        book.title = request.POST['book_title']
        book.authors.add(author)
        book.publisher = publisher
        book.publication_field = timezone.now()

        author.salutation = request.POST['author_salutation']
        author.name = request.POST['author_name']
        author.email = request.POST['author_email']

        publisher.name = request.POST['publisher_name']
        publisher.address = request.POST['publisher_address']
        publisher.website = request.POST['publisher_website']

        author.save()
        publisher.save()
        book.save()


        return redirect(reverse('books:index'))