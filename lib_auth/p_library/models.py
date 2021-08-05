from django.db import models

class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Publisher(models.Model):
    pub_name = models.TextField()

    def __str__(self):
        return self.pub_name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    cover = models.ImageField(upload_to='images', height_field='cover_height', width_field='cover_width', max_length=100)
    cover_height = models.PositiveIntegerField()
    cover_width = models.PositiveIntegerField()
    
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    copy_count = models.PositiveSmallIntegerField(default=1)
    reader = models.ForeignKey(
        'Reader', on_delete=models.SET_NULL,
        null=True, blank=True,
        default='',
        related_name='get_book')
    def __str__(self):
        return self.title


class Reader(models.Model):
    name = models.TextField()
    is_friend = models.BooleanField(default=True)

    def __str__(self):
        return self.name
