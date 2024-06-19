from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_ROLE =(
        ('client','client'),
        ('seller','seller'),
        ('admin','admin'),
    )
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True, default='profile_pics/default.jpg')
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    user_role = models.CharField(max_length=100,choices=USER_ROLE,default="client")

    def __str__(self) -> str:
        return self.username


class Cotegory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Books(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='book_image', blank=True, null=True)
    disckription = models.TextField()
    cotegory = models.ForeignKey(Cotegory, on_delete=models.CASCADE, related_name='books')
    is_stock = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.name

class Cart(models.Model):
    books = models.OneToOneField(Books, on_delete=models.CASCADE, related_name='cart')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.books.name}"

    @property
    def totle_price(self):
        return self.books.price * self.quantity


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client')
    date_of_birth = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='book_image', blank=True, null=True)

    def __str__(self) -> str:
        return self.user.first_name


class Seller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller')
    date_of_birth = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='book_image', blank=True, null=True)

    def __str__(self) -> str:
        return self.user.first_name


