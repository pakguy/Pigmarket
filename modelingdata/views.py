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
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/register.html', {'form': form})
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
    template_name = 'Sex/list.html'
    context_object_name = 'Sexs'
    paginate_by = 20
    ordering = ['-name']


class SexCreateView(CreateView):
    model = Sex
    form_class = SexForm
    template_name = 'Sex/form.html'
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
    template_name = 'Sex/form.html'
    success_url = reverse_lazy('Sex-list')

class SexDeleteView(DeleteView):
    model = Sex
    template_name = 'Sex/confirm_delete.html'
    success_url = reverse_lazy('Sex-list')



class TagsColourListView(ListView):
    model = TagsColour
    # template_name = 'another/renamed/TagsColour_list.html'
    template_name = 'TagsColour/list.html'
    context_object_name = 'TagsColours'
    paginate_by = 20
    ordering = ['-name']


class TagsColourCreateView(CreateView):
    model = TagsColour
    form_class = TagsColourForm
    template_name = 'TagsColour/form.html'
    success_url = reverse_lazy('TagsColour-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class TagsColourDetailView(DetailView):
    model = TagsColour
    template_name = 'TagsColour/detail.html'
    context_object_name = 'TagsColour'
class TagsColourUpdateView(UpdateView):
    model = TagsColour
    form_class = TagsColourForm
    template_name = 'TagsColour/form.html'
    success_url = reverse_lazy('TagsColour-list')

class TagsColourDeleteView(DeleteView):
    model = TagsColour
    template_name = 'TagsColour/confirm_delete.html'
    success_url = reverse_lazy('TagsColour-list')