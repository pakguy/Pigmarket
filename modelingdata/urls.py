
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import *
from django.views.generic import TemplateView

urlpatterns = [

    path('Breed', BreedListView.as_view(), name='Breed-list'),
    path('Breed/create/', BreedCreateView.as_view(), name='Breed-create'),
    path('<int:pk>/details/Breed', BreedDetailView.as_view(), name='Breed-detail'),
    path('<int:pk>/update/Breed', BreedUpdateView.as_view(), name='Breed-update'),
    path('<int:pk>/delete/Breed', BreedDeleteView.as_view(), name='Breed-delete'),

    path('TagsColour', TagsColourListView.as_view(), name='TagsColour-list'),
    path('TagsColour/create/', TagsColourCreateView.as_view(), name='TagsColour-create'),
    path('<int:pk>/details/TagsColour', TagsColourDetailView.as_view(), name='TagsColour-detail'),
    path('<int:pk>/update/TagsColour', TagsColourUpdateView.as_view(), name='TagsColour-update'),
    path('<int:pk>/delete/TagsColour', TagsColourDeleteView.as_view(), name='TagsColour-delete'),

    path('Sex', SexListView.as_view(), name='Sex-list'),
    path('Sex/create/', SexCreateView.as_view(), name='Sex-create'),
    path('<int:pk>/details/Sex', SexDetailView.as_view(), name='Sex-detail'),
    path('<int:pk>/update/Sex', SexUpdateView.as_view(), name='Sex-update'),
    path('<int:pk>/delete/Sex', SexDeleteView.as_view(), name='Sex-delete'),


    path('register/', views.register, name='register'),
    path('/', views.home, name='home'),
    
    # Logout confirmation (GET only)
    path('logout/confirm/', 
         TemplateView.as_view(template_name='account/logout_confirm.html'), 
         name='logout_confirm'),
    
    # Actual logout endpoint (POST only)
    path('logout/', 
         LogoutView.as_view(next_page='login'), 
         name='logout'),
    
    path('login/', LoginView.as_view(
        template_name='account/login.html',
        redirect_authenticated_user=True,
        success_url='home'
    ), name='login'),
    
    path('profile/', views.profile_view, name='profile'),
]

# from django.urls import path
# from django.contrib.auth.views import LoginView, LogoutView
# from . import views
# from django.views.generic import TemplateView

# urlpatterns = [
#     path('register/', views.register, name='register'),    
#     # path('logout/confirm/', TemplateView.as_view(template_name='account/logout_confirm.html'), name='logout_confirm'),
#     path('logout/confirm/', TemplateView.as_view(template_name='account/logout_confirm.html'), name='logout_confirm'),

#     path('login/', LoginView.as_view(
#         template_name='account/login.html',
#         redirect_authenticated_user=True,
#         success_url='profile'  # Redirect to profile after successful login
#     ), name='login'),
#     path('profile/', views.profile_view, name='profile'),
#     # path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
#     path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

# ]
# from django.urls import path
# from django.contrib.auth.views import LoginView, LogoutView
# from . import views

# urlpatterns = [
#     path('register/', views.register, name='register'),
#     # path('login/', LoginView.as_view(
#     #     template_name='account/login.html',  # Double-check this path
#     #     redirect_authenticated_user=True
#     # ), name='login'),
#     path('login/', LoginView.as_view(
#         template_name='account/login.html',
#         redirect_authenticated_user=True,
#         success_url='profile'  # Add this line
#     ), name='login'),
#     path('profile/', views.profile_view, name='profile'),
#     # path('login/', LoginView.as_view(
#     #     template_name='account/login.html',
#     #     redirect_authenticated_user=True
#     # ), name='login'),
#     # path('logout/', LogoutView.as_view(), name='logout'),
#     path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

# ]