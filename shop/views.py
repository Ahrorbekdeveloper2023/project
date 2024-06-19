from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.db.models import Q
from .forms import (LoginForm, RegisterForm, ProfileEditForm)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (Cotegory, Books, Cart, Client, Seller)

class HomeView(View):
    def get(self, request):
        books = Books.objects.filter(is_stock=True)
        count = Cart.objects.count()
        cotegory = Cotegory.objects.all()
        return render(request, 'shop/home.html', {'books': books, 'count':count, 'cotegory': cotegory})


class CotegoryView(View):
    def get(self, request, id):
        cotegory = Cotegory.objects.all()
        category = get_object_or_404(Cotegory, id=id)
        books = category.books.all()
        return render(request, 'shop/home.html', {'books':books, 'cotegory': cotegory})




class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "shop/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.user_role == 'admin':
                    return redirect('client:home')
                elif user.user_role == 'client':  
                    return redirect("shop:home")
                elif user.user_role == 'seller':
                    return redirect("shop:home")

        form = LoginForm()
        return render(request, "shop/login.html", {"form": form})

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "shop/register.html", {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data["password"]
            user.set_password(password)
            user.save()

            if user.user_role == "client":
                new_client = Client()
                new_client.user = user
                new_client.save()

            
            elif user.user_role == "seller":
                new_seller = Seller()
                new_seller.user = user
                new_seller.save()
            

            return redirect("shop:home")

        form = RegisterForm()
        return render(request, "shop/register.html", {"form": form})


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect("/")




class ProductDetailView(View):
    def get(self, request, book_id):
        books = get_object_or_404(Books, id=book_id)
        count = Cart.objects.count()
        cotegory = Cotegory.objects.all()
        return render(request, 'shop/detail.html', {'books': books, 'count':count, 'cotegory': cotegory})


    def post(self, request, book_id):
        books = get_object_or_404(Books, id=book_id)
        quantity = int(request.POST['cart'])
        if Cart.objects.filter(books=books).exists():
            cart = Cart.objects.filter(books=books).first()
            cart.quantity += quantity
            cart.save()
        else:
            cart = Cart()
            cart.books = books
            cart.quantity = quantity
            cart.save()
        return redirect('shop:home')


class CartDetailView(LoginRequiredMixin, View):
    def get(self, request):
        books = Cart.objects.all()
        count = Cart.objects.count()
        cotegory = Cotegory.objects.all()
        return render(request, 'shop/cart_detail.html', {'books': books, 'count':count, 'cotegory': cotegory})

def delete(request, delete_id):
    cart = get_object_or_404(Cart, id=delete_id)
    cart.delete()
    return redirect('shop:home')


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "shop/profile.html")


class ProfileEditView(LoginRequiredMixin, View):
    def get(self, request):
        form = ProfileEditForm(instance=request.user)
        return render(request, "shop/crud.html", context={"form": form})

    def post(self, request):
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data["password"]
            user.set_password(password)
            form.save()
            return redirect("erp:profile")

        form = ProfileEditForm(instance=request.user)
        return render(request, "shop/crud.html", context={"form": form})



class BooksListView(View):
    def get(self, request):
        if request.GET != {}:
            books = Books.objects.filter(
                Q(books__name__contains=request.GET["search"])
                | Q(books__cotegory__contains=request.GET["search"])
            )
        else:
            books = Books.objects.all()
        return render(request, "shop/home.html", {"books": books})

