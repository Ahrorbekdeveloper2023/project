from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from shop.permissionmixin import SellerRequiredMixin
from .forms import CreateBookForm
from shop.models import Books
from django.urls import reverse

class CreateBookView(SellerRequiredMixin, View):
    def get(self, request):
        form = CreateBookForm()
        return render(request, 'seller/crud.html', context={"form":form})
    
    def post(self, request):
        form = CreateBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop:home')
        return render(request, 'seller/crud.html', {'form': form})


class BookUpdateView(SellerRequiredMixin, View):
    def get(self, request, id):
        book = get_object_or_404(Books, id=id)
        form = CreateBookForm(instance=book)
        return render(request, 'seller/crud.html', {'form': form})

    def post(self, request, id):
        updat = get_object_or_404(Books, id=id)

        form = CreateBookForm(instance=updat)

        if request.method == 'POST':
            form = CreateBookForm(request.POST, request.FILES, instance=updat)  
            if form.is_valid():
                form.save()
                url = reverse('shop:detail', args=[id])
                return redirect(url)

        return render(request, 'seller/crud.html', context={'form':form})

def book_delete(request, id):
    delet = get_object_or_404(Books, id=id)
    delet.delete()
    return redirect('shop:home')
