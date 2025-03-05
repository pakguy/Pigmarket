from django import forms
from django.contrib.auth.models import User
# from . import models
from .models import Mating
from .models import Farrowing
from .models import Weaning
from .models import Inven
from .models import TestP
from datetime import date
from .models import Litter

from .models import Litter_allocation as allocate_L

class testPForm(forms.ModelForm):
    class Meta:
        model = TestP
        fields = ['date','status','health']
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'max': date.today().strftime('%Y-%m-%d'),
                    'class': 'form-control'
                }
            )
        }
        

class MatingForm(forms.ModelForm):
    class Meta:
        model = Mating
        fields = ['date','boar_id','sow_id']
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'max': date.today().strftime('%Y-%m-%d'),
                    'class': 'form-control'
                }
            )
        }
          
class FarrowingForm(forms.ModelForm):
    class Meta:
        model = Farrowing
        fields = ['date','boar_id','sow_id','number_born', 'mortality']
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'max': date.today().strftime('%Y-%m-%d'),
                    'class': 'form-control'
                }
            )
        }
                   
class WeaningForm(forms.ModelForm):
    class Meta:
        model = Weaning
        fields = ['birth_date','date_wean','no_wean','avg_weight', 'mortality']
        widgets = {
            'date_wean': forms.DateInput(
                attrs={
                    'type': 'date',
                    'max': date.today().strftime('%Y-%m-%d'),
                    'class': 'form-control'
                }
            )
        }
          

class InvenForm(forms.ModelForm):
    class Meta:
        model = Inven
        fields = ['number','tag_colour','breed','sex','birth_date','weight','status','arrival','location']
        widgets = {
            'birth_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'max': date.today().strftime('%Y-%m-%d'),
                    'class': 'form-control'
                }
            ),
            'arrival': forms.DateInput(
                attrs={
                    'type': 'date',
                    'max': date.today().strftime('%Y-%m-%d'),
                    'class': 'form-control'
                }
            )
        }
        

    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']
        if birth_date > date.today():
            raise forms.ValidationError("Birth date cannot be in the future")
        return birth_date



class LitterForm(forms.ModelForm):
    class Meta:
        model = Litter
        fields = ['number','sex']

class allocate_LForm(forms.ModelForm):
    class Meta:
        model = allocate_L
        fields = ['litter','farrowing']
          

