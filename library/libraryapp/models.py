from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Author(models.Model):
    First_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.First_name + ' ' + self.Last_name


class Book(models.Model):
    availabel = models.BooleanField(default=True)
    book_name = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    number_of_books = models.IntegerField()
    availabel_of_books = models.IntegerField(default=1)
    isbn = models.IntegerField()
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name + ',' + str(self.price)


class Member(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name + '  ' + str(self.phone_number)


class Book_issue(models.Model):
    date = models.DateField()
    return_date = models.DateField()
    availabel = models.ForeignKey(Member, null=True, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date) + ', ' + str(self.return_date)


@receiver(post_save, sender=Book_issue)
def is_borrowed(sender, instance, **kwargs):
    stock = instance.book.availabel_of_books
    if stock > 0:
        stock = stock-1
        book1 = instance.book
        instance.book.availabel_of_books = stock
        book1.save()
    return True
