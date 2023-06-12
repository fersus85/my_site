from django.views.generic import ListView, CreateView

from read.models import Book, Year


# Create your views here.
class ReadListView(ListView):
    model = Year
    template_name = "read/read_home.html"
    context_object_name = 'years'


class YearListView(ListView):
    model = Book
    template_name = "read/read_year.html"
    context_object_name = 'ooks'

    def get_queryset(self):
        return Book.objects.filter(year_id=self.kwargs["year_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["year"] = Year.objects.get(id=self.kwargs["year_id"])
        return context


class YearCreateView(CreateView):
    model = Year
    fields = ('title',)
    template_name = "read/read_create.html"


class BookCreateView(CreateView):
    model = Book
    fields = '__all__'
    template_name = "read/book_create.html"

