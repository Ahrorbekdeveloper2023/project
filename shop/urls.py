from django.urls import path
from .views import (HomeView, LoginView, LogoutView, RegisterView,
                    CotegoryView, ProductDetailView, CartDetailView, delete, ProfileView,
                    ProfileEditView, BooksListView)

app_name = 'shop'

urlpatterns = [ 
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('cotegory/<int:id>/', CotegoryView.as_view(), name='cotegory'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('detail/<int:book_id>/', ProductDetailView.as_view(), name='detail'),
    path('delete/<int:delete_id>/', delete, name='delete'),
    path('cart-detail/', CartDetailView.as_view(), name='cart_detail'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('update/', ProfileEditView.as_view(), name='update'),
    path('book/', BooksListView.as_view(), name='book'),

]

