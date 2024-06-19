from django.contrib import admin
from .models import User, Cotegory, Books, Cart, Client, Seller

admin.site.register([User, Cotegory, Books, Cart, Client, Seller])