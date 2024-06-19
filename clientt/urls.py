from django.urls import path
from .views import AdmminView, RegisterView, UsersView, UsersEditView, BooksReadView, ProfileView, HomeView, user_delete

app_name = 'client'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('users-table/', UsersView.as_view(), name='users_table'),
    path('users-edit/<int:id>', UsersEditView.as_view(), name='users_edit'),
    path('user-delete/<int:id>', user_delete, name='user_delete'),
    path('admin-dashboard/', AdmminView.as_view(), name='admin_dashboard'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('book-table/', BooksReadView.as_view(), name='book_table'),

]