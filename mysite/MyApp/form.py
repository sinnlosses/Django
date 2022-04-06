from django.forms import ModelForm
from MyApp.models import Book, Author, Memory

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('author',)

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title','start_date', 'end_date', 'author')

class MemoryForm(ModelForm):
    class Meta:
        model = Memory
        fields = ('title','text',)