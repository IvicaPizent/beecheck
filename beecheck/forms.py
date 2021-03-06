from django import forms
from django.core.exceptions import ObjectDoesNotExist

from bootstrap_datepicker_plus import DatePickerInput

from .models import Location, Hive

class AddLocationForm(forms.Form):
	location_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'autocomplete': 'off'}))

class AddHiveForm(forms.Form):
	hive_number = forms.IntegerField()

class AddNucleusForm(forms.Form):
	nucleus_number = forms.IntegerField()
	
class AddCheckForm(forms.Form):
	created_on = forms.DateField(widget=DatePickerInput())
	opened_honey = forms.DecimalField(max_digits=5, decimal_places=3, required=False)
	closed_honey = forms.DecimalField(max_digits=5, decimal_places=3, required=False)
	opened_brood = forms.DecimalField(max_digits=5, decimal_places=3, required=False)
	closed_brood = forms.DecimalField(max_digits=5, decimal_places=3, required=False)
	drone_cell = forms.DecimalField(max_digits=5, decimal_places=3, required=False)
	queen_cell = forms.IntegerField(required=False)
	pollen_cell = forms.DecimalField(max_digits=5, decimal_places=3, required=False)
	observation = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}), required=False)

class AddNucleusCheckForm(forms.Form):
	created_on = forms.DateField(widget=DatePickerInput())
	observation = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}), required=False)

class AddQueenForm(forms.Form):
	queen_name = forms.CharField(max_length=100)
	queen_added_date = forms.DateField(widget=DatePickerInput())
	queen_removed_date = forms.DateField(widget=DatePickerInput(), required=False)

class AddNoteForm(forms.Form):
	text = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))