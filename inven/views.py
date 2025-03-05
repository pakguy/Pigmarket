from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse 
from django.urls import reverse_lazy
from django.utils import timezone
from .models import *
from .models import Litter_allocation as allocate_L
from . import models
from .forms import *
from django.db.models import Q
# Create your views here.

class InvenListView(ListView):
    model = Inven
    # template_name = 'another/renamed/Inven_list.html'
    template_name = 'firstlabel/renamed/list.html'
    context_object_name = 'Invens'
    paginate_by = 20
    ordering = ['-birth_date']

    def get_context_data(self, **kwargs):
        """Add additional context to the template"""
        context = super().get_context_data(**kwargs)
        context.update({
            'current_date': timezone.now().date(),
            'search_query': self.request.GET.get('q', '')
        })
        return context

    def get_queryset(self):
        """Filter queryset based on search parameters"""
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        
        if search_query:
            # Search both name and birth date
            return queryset.filter(
                Q(name__icontains=search_query) |
                Q(birth_date__icontains=search_query)
            )
        return queryset


class InvenCreateView(CreateView):
    model = Inven
    form_class = InvenForm
    template_name = 'another/renamed/Inven_form.html'
    success_url = reverse_lazy('Inven-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class InvenDetailView(DetailView):
    model = Inven
    template_name = 'another/renamed/Inven_detail.html'
    context_object_name = 'Inven'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Inven = self.get_object()
        context['age'] = {
            'years': Inven.age_components[0],
            'months': Inven.age_components[1],
            'days': Inven.age_components[2]
        }
        return context

class InvenUpdateView(UpdateView):
    model = Inven
    form_class = InvenForm
    template_name = 'another/renamed/Inven_form.html'
    success_url = reverse_lazy('Inven-list')

class InvenDeleteView(DeleteView):
    model = Inven
    template_name = 'another/renamed/Inven_confirm_delete.html'
    success_url = reverse_lazy('Inven-list')

# TestP view


class TestPListView(ListView):
    model = TestP
    # template_name = 'another/renamed/TestP_list.html'
    template_name = 'testp/list.html'
    context_object_name = 'TestPs'
    paginate_by = 20
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        """Add additional context to the template"""
        context = super().get_context_data(**kwargs)
        context.update({
            'current_date': timezone.now().date(),
            'search_query': self.request.GET.get('q', '')
        })
        return context

    def get_queryset(self):
        """Filter queryset based on search parameters"""
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        
        if search_query:
            # Search both name and birth date
            return queryset.filter(
                Q(name__icontains=search_query) |
                Q(birth_date__icontains=search_query)
            )
        return queryset


class TestPCreateView(CreateView):
    model = TestP
    form_class = testPForm
    template_name = 'testp/form.html'
    success_url = reverse_lazy('TestP-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class TestPDetailView(DetailView):
    model = TestP
    template_name = 'testp/detail.html'
    context_object_name = 'TestP'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     TestP = self.get_object()
    #     context['age'] = {
    #         'years': TestP.age_components[0],
    #         'months': TestP.age_components[1],
    #         'days': TestP.age_components[2]
    #     }
    #     return context

class TestPUpdateView(UpdateView):
    model = TestP
    form_class = testPForm
    template_name = 'testp/form.html'
    success_url = reverse_lazy('TestP-list')

class TestPDeleteView(DeleteView):
    model = TestP
    template_name = 'testp/confirm_delete.html'
    success_url = reverse_lazy('TestP-list')





class MatingListView(ListView):
    model = Mating
    # template_name = 'another/renamed/Mating_list.html'
    template_name = 'mating/list.html'
    context_object_name = 'Matings'
    paginate_by = 20
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        """Add additional context to the template"""
        context = super().get_context_data(**kwargs)
        context.update({
            'current_date': timezone.now().date(),
            'search_query': self.request.GET.get('q', '')
        })
        return context

    def get_queryset(self):
        """Filter queryset based on search parameters"""
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        
        if search_query:
            # Search both name and birth date
            return queryset.filter(
                Q(name__icontains=search_query) |
                Q(date__icontains=search_query)
            )
        return queryset


class MatingCreateView(CreateView):
    model = Mating
    form_class = MatingForm
    template_name = 'mating/form.html'
    success_url = reverse_lazy('Mating-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class MatingDetailView(DetailView):
    model = Mating
    template_name = 'mating/detail.html'
    context_object_name = 'Mating'
class MatingUpdateView(UpdateView):
    model = Mating
    form_class = MatingForm
    template_name = 'mating/form.html'
    success_url = reverse_lazy('Mating-list')

class MatingDeleteView(DeleteView):
    model = Mating
    template_name = 'mating/confirm_delete.html'
    success_url = reverse_lazy('Mating-list')
# 
# 



class LitterListView(ListView):
    model = Litter
    # template_name = 'another/renamed/Litter_list.html'
    template_name = 'litter/list.html'
    context_object_name = 'Litters'
    paginate_by = 20
    ordering = ['-number']


class LitterCreateView(CreateView):
    model = Litter
    form_class = LitterForm
    template_name = 'litter/form.html'
    success_url = reverse_lazy('Litter-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class LitterDetailView(DetailView):
    model = Litter
    template_name = 'litter/detail.html'
    context_object_name = 'Litter'
class LitterUpdateView(UpdateView):
    model = Litter
    form_class = LitterForm
    template_name = 'litter/form.html'
    success_url = reverse_lazy('Litter-list')

class LitterDeleteView(DeleteView):
    model = Litter
    template_name = 'Litter/confirm_delete.html'
    success_url = reverse_lazy('Litter-list')
# 

class FarrowingListView(ListView):
    model = Farrowing
    # template_name = 'another/renamed/Farrowing_list.html'
    template_name = 'Farrowing/list.html'
    context_object_name = 'Farrowings'
    paginate_by = 20
    ordering = ['-date']

    # def get_context_data(self, **kwargs):
    #     """Add additional context to the template"""
    #     context = super().get_context_data(**kwargs)
    #     context.update({
    #         'current_date': timezone.now().date(),
    #         'search_query': self.request.GET.get('q', '')
    #     })
    #     return context

    # def get_queryset(self):
    #     """Filter queryset based on search parameters"""
    #     queryset = super().get_queryset()
    #     search_query = self.request.GET.get('q')
        
    #     if search_query:
    #         # Search both name and birth date
    #         return queryset.filter(
    #             Q(name__icontains=search_query) |
    #             Q(birth_date__icontains=search_query)
    #         )
    #     return queryset


class FarrowingCreateView(CreateView):
    model = Farrowing
    form_class = FarrowingForm
    template_name = 'Farrowing/form.html'
    success_url = reverse_lazy('Farrowing-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class FarrowingDetailView(DetailView):
    model = Farrowing
    template_name = 'Farrowing/detail.html'
    context_object_name = 'Farrowing'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     Farrowing = self.get_object()
    #     context['age'] = {
    #         'years': Farrowing.age_components[0],
    #         'months': Farrowing.age_components[1],
    #         'days': Farrowing.age_components[2]
    #     }
    #     return context

class FarrowingUpdateView(UpdateView):
    model = Farrowing
    form_class = FarrowingForm
    template_name = 'Farrowing/form.html'
    success_url = reverse_lazy('Farrowing-list')

class FarrowingDeleteView(DeleteView):
    model = Farrowing
    template_name = 'Farrowing/confirm_delete.html'
    success_url = reverse_lazy('Farrowing-list')

# 
# 



# def farrowing_details(request, birthdetail):
#     birth = models.Farrowing.objects.filter(pk=birthdetail)
#     litter = models.Litter.objects.filter(pk=birthdetail)

#     context ={
#         'litter': litter,
#         'birth' : birth
#     }
#     return render(request,'First1/Litter/birthdetail.html', context)
    


def farrowing_details(request, birthdetail):
    # Fetch a single Farrowing object using the ID from the URL
    birth = get_object_or_404(models.Farrowing, pk=birthdetail)
    # litter = get_object_or_404(models.Litter, pk=birthdetail)

    litter = models.Litter.objects.filter(litter_allocation__farrowing=birth)
    
    # Fetch related Litter (assuming Farrowing has a ForeignKey to Litter)
    # litter = birth.Litter.all()  # If using a reverse relationship
    # Or if Litter has a ForeignKey to Farrowing:
    # litter = models.Litter.objects.filter(pk=birthdetail)
    
    context = {
        'litter': litter,
        'birth': birth
    }
    return render(request, 'First1/Litter/birthdetail.html', context)
# 

def your_view(request):
    farrowing = models.Farrowing.objects.all()
    
    context = {
        'farrowing': farrowing,
    }
    return render(request, 'First1/Litter/listdetail.html', context)


# 
# 
# 

class WeaningListView(ListView):
    model = Weaning
    template_name = 'Weaning/list.html'
    context_object_name = 'Weanings'
    paginate_by = 20
    ordering = ['-date_wean']

    def get_context_data(self, **kwargs):
        """Add additional context to the template"""
        context = super().get_context_data(**kwargs)
        context.update({
            'current_date': timezone.now().date(),
            'search_query': self.request.GET.get('q', '')
        })
        return context

    def get_queryset(self):
        """Filter queryset based on search parameters"""
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        
        if search_query:
            # Search both name and birth date
            return queryset.filter(
                Q(name__icontains=search_query) |
                Q(birth_date__icontains=search_query)
            )
        return queryset


class WeaningCreateView(CreateView):
    model = Weaning
    form_class = WeaningForm
    template_name = 'Weaning/form.html'
    success_url = reverse_lazy('Weaning-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class WeaningDetailView(DetailView):
    model = Weaning
    template_name = 'Weaning/detail.html'
    context_object_name = 'Weaning'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Weaning = self.get_object()
        context['age'] = {
            'years': Weaning.age_components[0],
            'months': Weaning.age_components[1],
            'days': Weaning.age_components[2]
        }
        return context

class WeaningUpdateView(UpdateView):
    model = Weaning
    form_class = WeaningForm
    template_name = 'Weaning/form.html'
    success_url = reverse_lazy('Weaning-list')

class WeaningDeleteView(DeleteView):
    model = Weaning
    template_name = 'Weaning/confirm_delete.html'
    success_url = reverse_lazy('Weaning-list')


# 
# 
# 

class InvenListView(ListView):
    model = Inven
    template_name = 'inven/Inven_list.html'
    # template_name = 'inven/list.html'
    context_object_name = 'Invens'
    paginate_by = 20
    ordering = ['-birth_date']

    def get_context_data(self, **kwargs):
        """Add additional context to the template"""
        context = super().get_context_data(**kwargs)
        context.update({
            'current_date': timezone.now().date(),
            'search_query': self.request.GET.get('q', '')
        })
        return context

    def get_queryset(self):
        """Filter queryset based on search parameters"""
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        
        if search_query:
            # Search both name and birth date
            return queryset.filter(
                Q(name__icontains=search_query) |
                Q(birth_date__icontains=search_query)
            )
        return queryset


class InvenCreateView(CreateView):
    model = Inven
    form_class = InvenForm
    template_name = 'inven/Inven_form.html'
    success_url = reverse_lazy('Inven-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class InvenDetailView(DetailView):
    model = Inven
    template_name = 'inven/Inven_detail.html'
    context_object_name = 'Inven'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Inven = self.get_object()
        context['age'] = {
            'years': Inven.age_components[0],
            'months': Inven.age_components[1],
            'days': Inven.age_components[2]
        }
        return context

class InvenUpdateView(UpdateView):
    model = Inven
    form_class = InvenForm
    template_name = 'inven/Inven_form.html'
    success_url = reverse_lazy('Inven-list')

class InvenDeleteView(DeleteView):
    model = Inven
    template_name = 'inven/Inven_confirm_delete.html'
    success_url = reverse_lazy('Inven-list')




class allocate_LListView(ListView):
    model = allocate_L
    # template_name = 'another/renamed/allocate_L_list.html'
    template_name = 'allocate_L/list.html'
    context_object_name = 'allocate_Ls'
    paginate_by = 20
    ordering = ['-litter']


class allocate_LCreateView(CreateView):
    model = allocate_L
    form_class = allocate_LForm
    template_name = 'allocate_L/form.html'
    success_url = reverse_lazy('allocate_L-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class allocate_LDetailView(DetailView):
    model = allocate_L
    template_name = 'allocate_L/detail.html'
    context_object_name = 'allocate_L'
class allocate_LUpdateView(UpdateView):
    model = allocate_L
    form_class = allocate_LForm
    template_name = 'allocate_L/form.html'
    success_url = reverse_lazy('allocate_L-list')

class allocate_LDeleteView(DeleteView):
    model = allocate_L
    template_name = 'allocate_L/confirm_delete.html'
    success_url = reverse_lazy('allocate_L-list')