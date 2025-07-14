from django.db import models

class Book(models.Model):
    """
    Book model representing a book in the library system.
    
    Attributes:
        title (str): The title of the book (max 200 characters)
        author (str): The author of the book (max 100 characters)
        publication_year (int): The year the book was published
    """
    
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        """
        String representation of the Book model.
        Returns the title and author of the book.
        """
        return f"{self.title} by {self.author}"
    
    class Meta:
        """
        Meta class for Book model configuration.
        """
        ordering = ['title']  # Default ordering by title
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
