from django.db import models

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from django.utils.translation import gettext_lazy as _ 
from modelingdata.models import (
    Breeds,
    TagsColour,
    Sex,
)

class Litter(models.Model):
    number = models.IntegerField(_("Litter ID"))
    sex = models.ForeignKey(Sex, verbose_name=_("Sex"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Litter")
        verbose_name_plural = _("Litters")

    def __str__(self):
        return f"{self.number} - {self.sex}"

    def get_absolute_url(self):
        return reverse("Litter_detail", kwargs={"pk": self.pk})

# Create your models here.
class Inven(models.Model):

    number = models.IntegerField(_("Pig ID"))
    tag_colour = models.ForeignKey(TagsColour,related_name='tagcolour', on_delete=models.CASCADE)
    breed = models.ForeignKey(Breeds, related_name='breed', on_delete=models.CASCADE)
    sex = models.ForeignKey(Sex, related_name='sex', on_delete=models.CASCADE)
    birth_date = models.DateField(_("Birth Date"), auto_now=False, auto_now_add=False)
    weight = models.IntegerField(_("Weight (kg)"))
    status = models.CharField(_("Health status"), max_length=100)
    arrival =models.DateField(_("arrival date"), auto_now=False, auto_now_add=False)
    location = models.CharField(_("address of seller farm"), max_length=255)

    def __str__(self):
        return f"{self.number} - {self.tag_colour} - {self.breed} - {self.sex} - {self.birth_date} - {self.weight} kg - {self.status} - {self.arrival} - {self.location}"
    

    def clean(self):
        if self.birth_date > date.today():
            raise ValidationError("Birth date cannot be in the future")

    
    def get_age(self) -> dict:
        """Return age as a dictionary with years, months, and days"""
        today = date.today()
        delta = relativedelta(today, self.birth_date)
        return {
            'years': delta.years,
            'months': delta.months,
            'days': delta.days
        }
    @property
    def age_string(self) -> str:
        """Formatted age string (e.g., '2 years, 3 months, 15 days')"""
        age = self.get_age()
        return f"{age['years']} years, {age['months']} months, {age['days']} days"

    @property        
    def age_components(self) -> tuple:
        """Return age as a tuple (years, months, days)"""
        age = self.get_age()
        return (age['years'], age['months'], age['days'])

    # def __str__(self) -> str:
    #     return f"Born: {self.birth_date.strftime('%Y-%m-%d')} | Age: {self.age_string}"

    class Meta:
        verbose_name_plural = "Invens"
        ordering = ['-birth_date']


class Mating(models.Model):
    date = models.DateField(_("Mating Date"))
    boar_id = models.ForeignKey(
        Inven,
        on_delete=models.CASCADE,
        verbose_name=_("Boar"),
        limit_choices_to={'sex__name': 'BOAR'},  # Filter only Boars
        related_name='matings_as_boar'
    )
    sow_id = models.ForeignKey(
        Inven,
        on_delete=models.CASCADE,
        verbose_name=_("Sow"),
        limit_choices_to={'sex__name': 'SOW'},  # Filter only Sows
        related_name='matings_as_sow'
    )

    def __str__(self):
        return f"Mating on {self.date} for Tag {self.boar_id.number} - {self.boar_id.tag_colour}- {self.boar_id.breed} and for Tag {self.sow_id.number} - {self.sow_id.tag_colour}- {self.sow_id.breed}"





class TestP(models.Model):
    date = models.ForeignKey(Mating, verbose_name=_("Mating Date"), on_delete=models.CASCADE)
    status = models.CharField(_("Status"), max_length=100)
    health = models.CharField(_("Health"), max_length=100)

    @property
    def delivery(self):
        # Calculate delivery date as 50 days after the mating date
        return self.date.date + timedelta(days=50)

    def __str__(self):
        return f"{self.date} - {self.status} - {self.health} - Delivery: {self.delivery}"








class Farrowing(models.Model):
    date = models.DateField(_("Date"), auto_now=False, auto_now_add=False) 
    boar_id = models.ForeignKey(
        Inven,
        on_delete=models.CASCADE,
        verbose_name=_("Boar"),
        limit_choices_to={'sex__name': 'BOAR'},  # Filter only Boars
        related_name='fallowing_as_boar'
    )
    sow_id = models.ForeignKey(
        Inven,
        on_delete=models.CASCADE,
        verbose_name=_("Sow"),
        limit_choices_to={'sex__name': 'SOW'},  # Filter only Sows
        related_name='farrowing_as_soW'
    )
    number_born = models.IntegerField(_("No. Born"))
    mortality = models.IntegerField(_("Mortality"))

    @property
    def total_left(self):
        return self.number_born - self.mortality
    @property
    def weaning(self):
        return self.date + timedelta(days=30)
    def __str__(self):
        return f"{self.date} Boar: {self.boar_id.id} - Sow: {self.sow_id.id} - no. born: {self.number_born} - mortality{self.mortality} total left{self.total_left} - weaning date {self.weaning}"


    class Meta:
        verbose_name = _("Farrowing")
        verbose_name_plural = _("Farrowings")

    def get_absolute_url(self):
        return reverse("Farrowing_detail", kwargs={"pk": self.pk})



# weaning


class Weaning(models.Model):
    birth_date = models.ForeignKey(Farrowing, verbose_name=_("Date farrowed"), on_delete=models.CASCADE)
    date_wean = models.DateField(_("weaning date"), auto_now=False, auto_now_add=False)
    no_wean = models.IntegerField(_("number Wean"))
    avg_weight = models.IntegerField(_("Average Weight"))
    mortality = models.IntegerField(_("mortality after farrowing"))
    @property
    def no_of_litters(self):
        # Count the number of Litter objects associated with the Farrowing instance
        return Litter.objects.filter(id=self.birth_date.litter_id.id).count()

    @property
    def total_left(self):
        # Calculate total left as total_left from Farrowing minus mortality from Weaning
        return self.birth_date.total_left - self.mortality
    @property
    def maturity(self):
        return self.birth_date.date + timedelta(days=200)
    
    @property
    def current_litter_age(self):
        if self.birth_date.date > date.today():
            raise ValidationError("Birth date cannot be in the future")

    
    def get_age(self) -> dict:
        """Return age as a dictionary with years, months, and days"""
        today = date.today()
        delta = relativedelta(today, self.birth_date.date)
        return {
            'years': delta.years,
            'months': delta.months,
            'days': delta.days
        }
    @property
    def age_string(self) -> str:
        """Formatted age string (e.g., '2 years, 3 months, 15 days')"""
        age = self.get_age()
        return f"{age['years']} years, {age['months']} months, {age['days']} days"

    @property        
    def age_components(self) -> tuple:
        """Return age as a tuple (years, months, days)"""
        age = self.get_age()
        return (age['years'], age['months'], age['days'])
    class Meta:
        verbose_name = _("Weaning")
        verbose_name_plural = _("Weanings")

    # def __str__(self):
    #     return f"Weaning on {self.date_wean} for Farrowing on {self.birth_date.date} - No. of Litters: {self.no_of_litters}"


    def __str__(self):
        return f"Weaning on {self.date_wean} for Farrowing on {self.birth_date.date} - No. Weaned: {self.no_wean} - Total Left: {self.total_left} - current age{self.age_string}"

    def get_absolute_url(self):
        return reverse("Weaning_detail", kwargs={"pk": self.pk})



class Litter_allocation(models.Model):
    litter = models.ForeignKey(Litter, verbose_name=_("Litter"), on_delete=models.CASCADE)
    farrowing = models.ForeignKey(Farrowing, verbose_name=_("Farrowing"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Litter_allocation")
        verbose_name_plural = _("Litter_allocations")

    def __str__(self):
        return f" {self.farrowing} with {self.litter}"

    def get_absolute_url(self):
        return reverse("Litter_allocation_detail", kwargs={"pk": self.pk})
