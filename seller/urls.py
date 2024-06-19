from django.urls import path
from .views import CreateBookView, BookUpdateView, book_delete

app_name = 'seller'

urlpatterns = [
    path('create/', CreateBookView.as_view(), name='create'),
    path('update/<int:id>/', BookUpdateView.as_view(), name='update'),
    path('delete/<int:id>/', book_delete, name='delete'),

]