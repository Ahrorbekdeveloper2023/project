from django.shortcuts import render, redirect, get_object_or_404
from shop.permissionmixin import AdminRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import UserEditForm
from shop.models import Seller, User, Books, Client
from shop.forms import (SellerRegisterForm)



class AdmminView(AdminRequiredMixin, View):
    def get(self, request):
        return render(request, 'clientt/dashboard.html')


class HomeView(View):
    def get(self, request):
        books = Books.objects.filter(is_stock=True)
        return render(request, 'clientt/home.html', {'books': books})


class RegisterView(AdminRequiredMixin, View):
    def get(self, request):
        form = SellerRegisterForm()
        return render(request, "clientt/register.html", {"form": form})

    def post(self, request):
        form = SellerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data["password"]
            user.set_password(password)
            user.save()

            if user.user_role == "seller":
                new_seller = Seller()
                new_seller.user = user
                new_seller.save()
            

            return redirect("client:users_table")

        form = SellerRegisterForm()
        return render(request, "clientt/register.html", {"form": form})

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "clientt/profile.html")

class UsersView(AdminRequiredMixin, View):
    def get(self, request):
        user = User.objects.all()
        return render(request, "clientt/users.html", {"user": user})


class UsersEditView(AdminRequiredMixin, View):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        form = UserEditForm(instance=user)
        return render(request, "clientt/crud.html", context={"form": form})

    def post(self, request, id):
        user = get_object_or_404(User, id=id)
        form = UserEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data["password"]
            user.set_password(password)
            form.save()
    
            if user.user_role == "client":
                new_client = Client()
                new_client.user = user
                new_client.save()

            
            elif user.user_role == "seller":
                new_seller = Seller()
                new_seller.user = user
                new_seller.save()

            return redirect("client:users_table")

        form = UserEditForm(instance=request.user)
        return render(request, "clientt/crud.html", context={"form": form})

def user_delete(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect("client:users_table")


class BooksReadView(AdminRequiredMixin, View):
    def get(self, request):
        books = Books.objects.all()
        return render(request, "clientt/books.html", {"books":books})