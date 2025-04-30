from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('author-detail', kwargs={'pk': self.pk})


class Book(models.Model):
    APPROPRIATE_AGE_CHOICES = [
        ('UNDER_8', 'Under 8'),
        ('8_15', '8-15'),
        ('ADULTS', 'Adults'),
    ]

    title = models.CharField(max_length=200)
    publish_date = models.DateField()
    add_to_site_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='book_covers/', null=True, blank=True)

    appropriate_age = models.CharField(
        max_length=7,
        choices=APPROPRIATE_AGE_CHOICES,
        default='ADULTS'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/books/{self.id}/"