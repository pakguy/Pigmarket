# views.py
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse 
from django.urls import reverse_lazy
from django.utils import timezone
from .models import *
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Breeds as Breed
from django.contrib.auth.models import User, auth
from django.contrib.auth.views import LoginView

def confirm_logout(request):
    return render(request, 'account/logout_confirm.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

class CustomLoginView(LoginView):
    template_name = 'account/login.html'  # Specify your login template

    def form_valid(self, form):
        # Call the parent class's form_valid method to log the user in
        response = super().form_valid(form)
        
        # Redirect to the desired URL after successful login
        return redirect('home')  # Change 'home' to the desired redirect URL

    def get_success_url(self):
        # This method can be used to define the success URL
        return reverse_lazy('home') 
@login_required
def profile_view(request):
    return render(request, 'account/profile.html')


@login_required
def home(request):
    return render(request, 'account/index.html')
    

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect('/')  # Redirect to home or another page
        else:
            # Print form errors to the console for debugging
            print(form.errors)  # You can also use logging here
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'account/register.html', {'form': form})
# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Auto-login after registration
#             return redirect('/')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'account/register.html', {'form': form})
# Create your views here.




class BreedListView(ListView):
    model = Breed
    # template_name = 'another/renamed/Breed_list.html'
    template_name = 'Breed/list.html'
    context_object_name = 'Breedss'
    paginate_by = 20
    ordering = ['-name']


class BreedCreateView(CreateView):
    model = Breed
    form_class = BreedForm
    template_name = 'Breed/form.html'
    success_url = reverse_lazy('Breed-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class BreedDetailView(DetailView):
    model = Breed
    template_name = 'Breed/detail.html'
    context_object_name = 'Breed'
class BreedUpdateView(UpdateView):
    model = Breed
    form_class = BreedForm
    template_name = 'Breed/form.html'
    success_url = reverse_lazy('Breed-list')

class BreedDeleteView(DeleteView):
    model = Breed
    template_name = 'Breed/confirm_delete.html'
    success_url = reverse_lazy('Breed-list')



class SexListView(ListView):
    model = Sex
    # template_name = 'another/renamed/Sex_list.html'
    template_name = 'sex/list.html'
    context_object_name = 'Sexs'
    paginate_by = 20
    ordering = ['-name']


class SexCreateView(CreateView):
    model = Sex
    form_class = SexForm
    template_name = 'sex/form.html'
    success_url = reverse_lazy('Sex-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class SexDetailView(DetailView):
    model = Sex
    template_name = 'Sex/detail.html'
    context_object_name = 'Sex'
class SexUpdateView(UpdateView):
    model = Sex
    form_class = SexForm
    template_name = 'sex/form.html'
    success_url = reverse_lazy('Sex-list')

class SexDeleteView(DeleteView):
    model = Sex
    template_name = 'sex/confirm_delete.html'
    success_url = reverse_lazy('Sex-list')



class TagsColourListView(ListView):
    model = TagsColour
    # template_name = 'another/renamed/TagsColour_list.html'
    template_name = 'tagcolour/list.html'
    context_object_name = 'TagsColours'
    paginate_by = 20
    ordering = ['-name']


class TagsColourCreateView(CreateView):
    model = TagsColour
    form_class = TagsColourForm
    template_name = 'tagcolour/form.html'
    success_url = reverse_lazy('TagsColour-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class TagsColourDetailView(DetailView):
    model = TagsColour
    template_name = 'tagcolour/detail.html'
    context_object_name = 'TagsColour'
class TagsColourUpdateView(UpdateView):
    model = TagsColour
    form_class = TagsColourForm
    template_name = 'tagcolour/form.html'
    success_url = reverse_lazy('TagsColour-list')

class TagsColourDeleteView(DeleteView):
    model = TagsColour
    template_name = 'tagcolour/confirm_delete.html'
    success_url = reverse_lazy('TagsColour-list')