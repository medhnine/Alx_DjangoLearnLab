from django.db import models

class Author(models.Model):
    """
    Author model representing book authors.
    """
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Book(models.Model):
    """
    Book model with ForeignKey relationship to Author.
    """
    title = models.CharField(max_length=300)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    def __str__(self):
        return f"{self.title} by {self.author.name}"
    
    class Meta:
        ordering = ['title']

class Library(models.Model):
    """
    Library model with ManyToMany relationship to Book.
    """
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='libraries')
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Libraries"

class Librarian(models.Model):
    """
    Librarian model with OneToOne relationship to Library.
    """
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')
    
    def __str__(self):
        return f"{self.name} (Librarian at {self.library.name})"
    
    class Meta:
        ordering = ['name']
