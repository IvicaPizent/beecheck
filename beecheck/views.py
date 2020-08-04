from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView, FormView, UpdateView

from .forms import *
from .models import *

from random import randint
from bootstrap_datepicker_plus import DatePickerInput

def index(request):
	loc = Location.objects.order_by('location_name')

	context = {
		'loc': loc
	}

	return render(request, 'index.html', context)

def location(request, location):
	loc = Location.objects.get(location_id=location)
	hives = Hive.objects.filter(location_id=loc.location_id).order_by('hive_number')
	nucleuses = Nucleus.objects.filter(location_id=loc.location_id).order_by('nucleus_number')

	context = {
		'loc': loc,
		'hives': hives,
		'nucleuses': nucleuses,
	}

	return render(request, 'location.html', context)

def hive(request, hive):
	hive = Hive.objects.get(hive_id=hive)
	checks = Check.objects.filter(hive_id=hive.hive_id).order_by('-created_on')
	queens = Queen.objects.filter(hive_id=hive.hive_id).order_by('-queen_added_date')

	context = {
		'hive': hive,
		'checks': checks,
		'queens': queens,
	}

	return render(request, 'hive.html', context)

def nucleus(request, nucleus):
	nucleus = Nucleus.objects.get(nucleus_id=nucleus)
	nucleus_checks = NucleusCheck.objects.filter(nucleus_id=nucleus.nucleus_id).order_by('-created_on')
	nucleus_queens = NucleusQueen.objects.filter(nucleus_id=nucleus.nucleus_id).order_by('-queen_added_date')

	context = {
		'nucleus': nucleus,
		'nucleus_checks': nucleus_checks,
		'nucleus_queens': nucleus_queens,
	}

	return render(request, 'nucleus.html', context)

def check(request, check):
	check = Check.objects.get(check_id=check)
	
	context = {
		'check': check,
	}

	return render(request, 'check.html', context)

def nucleus_check(request, nucleus_check):
	nucleus_check = NucleusCheck.objects.get(nucleus_check_id=nucleus_check)

	context = {
		'nucleus_check': nucleus_check,
	}

	return render(request, 'nucleus_check.html', context)

def queen(request, queen):
	queen = Queen.objects.get(queen_id=queen)

	context = {
		'queen': queen,
	}

	return render(request, 'queen.html', context)

def nucleus_queen(request, nucleus_queen):
	nucleus_queen = NucleusQueen.objects.get(nucleus_queen_id=nucleus_queen)

	context = {
		'nucleus_queen': nucleus_queen,
	}

	return render(request, 'nucleus_queen.html', context)

def notes(request, notes):
	hive = Hive.objects.get(hive_id=notes)
	notes = Note.objects.filter(hive_id=notes).order_by('-created_on')

	context = {
		'hive': hive,
		'notes': notes,
	}

	return render(request, 'notes.html', context)

class AddLocationFormView(FormView):
	form_class = AddLocationForm
	template_name = 'add_location.html'

	def form_valid(self, form):
		location_data = Location(
			location_name=form.cleaned_data['location_name']
		)
		location_data.save()
		return HttpResponseRedirect(reverse('index'))

class AddHiveFormView(FormView):
	form_class = AddHiveForm
	template_name = 'add_hive.html'

	def get_context_data(self, **kwargs):
		loc = Location.objects.filter(location_id__contains=self.kwargs['location'])
		kwargs['loc'] = loc[0]
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		loc = Location.objects.filter(location_id__contains=self.kwargs['location'])

		hive_data = Hive(
			hive_number=form.cleaned_data['hive_number'],
			location_id=loc[0],
		)
		hive_data.save()
		return HttpResponseRedirect(reverse('location', args=[loc[0].location_id]))

class AddNucleusFormView(FormView):
	form_class = AddNucleusForm
	template_name = 'add_nucleus.html'

	def get_context_data(self, **kwargs):
		loc = Location.objects.filter(location_id__contains=self.kwargs['location'])
		kwargs['loc'] = loc[0]
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		loc = Location.objects.filter(location_id__contains=self.kwargs['location'])

		nucleus_data = Nucleus(
			nucleus_number=form.cleaned_data['nucleus_number'],
			location_id=loc[0],
		)
		nucleus_data.save()
		return HttpResponseRedirect(reverse('location', args=[loc[0].location_id]))

class AddCheckFormView(FormView):
	form_class = AddCheckForm
	template_name = 'add_check.html'

	'''def get_form(self):
		form = super().get_form()
		form.fields['created_on'].widget = DatePickerInput()
		return form'''

	def get_context_data(self, **kwargs):
		hive = Hive.objects.filter(hive_id__contains=self.kwargs['hive'])
		kwargs['hive'] = hive[0]
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		hive = Hive.objects.filter(hive_id__contains=self.kwargs['hive'])

		if form.cleaned_data['opened_honey'] == None:
			opened_honey_default = '0.000'
		else:
			opened_honey_default = form.cleaned_data['opened_honey']
		if form.cleaned_data['closed_honey'] == None:
			closed_honey_default = '0.000'
		else:
			closed_honey_default = form.cleaned_data['closed_honey']
		if form.cleaned_data['opened_brood'] == None:
			opened_brood_default = '0.000'
		else:
			opened_brood_default = form.cleaned_data['opened_brood']
		if form.cleaned_data['closed_brood'] == None:
			closed_brood_default = '0.000'
		else:
			closed_brood_default = form.cleaned_data['closed_brood']
		if form.cleaned_data['drone_cell'] == None:
			drone_cell_default = '0.000'
		else:
			drone_cell_default = form.cleaned_data['drone_cell']
		if form.cleaned_data['queen_cell'] == None:
			queen_cell_default = '0'
		else:
			queen_cell_default = form.cleaned_data['queen_cell']
		if form.cleaned_data['pollen_cell'] == None:
			pollen_cell_default = '0.000'
		else:
			pollen_cell_default = form.cleaned_data['pollen_cell']

		check_data = Check(
			created_on=form.cleaned_data['created_on'],
			opened_honey=opened_honey_default,
			closed_honey=closed_honey_default,
			opened_brood=opened_brood_default,
			closed_brood=closed_brood_default,
			drone_cell=drone_cell_default,
			queen_cell=queen_cell_default,
			pollen_cell=pollen_cell_default,
			observation=form.cleaned_data['observation'],
			hive_id=hive[0],
		)
		check_data.save()
		return HttpResponseRedirect(reverse('hive', args=[hive[0].hive_id]))

class AddNucleusCheckFormView(FormView):
	form_class = AddNucleusCheckForm
	template_name = 'add_nucleus_check.html'

	def get_context_data(self, **kwargs):
		nucleus = Nucleus.objects.filter(nucleus_id__contains=self.kwargs['nucleus'])
		kwargs['nucleus'] = nucleus[0]
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		nucleus = Nucleus.objects.filter(nucleus_id__contains=self.kwargs['nucleus'])

		nucleus_check_data = NucleusCheck(
			created_on=form.cleaned_data['created_on'],
			observation=form.cleaned_data['observation'],
			nucleus_id=nucleus[0],
		)
		nucleus_check_data.save()
		return HttpResponseRedirect(reverse('nucleus', args=[nucleus[0].nucleus_id]))

class AddQueenFormView(FormView):
	form_class = AddQueenForm
	template_name = 'add_queen.html'

	def get_context_data(self, **kwargs):
		hive = Hive.objects.filter(hive_id__contains=self.kwargs['hive'])
		kwargs['hive'] = hive[0]
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		hive = Hive.objects.filter(hive_id__contains=self.kwargs['hive'])

		queen_data = Queen(
			queen_name=form.cleaned_data['queen_name'],
			queen_added_date=form.cleaned_data['queen_added_date'],
			queen_removed_date=form.cleaned_data['queen_removed_date'],
			hive_id=hive[0],
		)
		queen_data.save()
		return HttpResponseRedirect(reverse('hive', args=[hive[0].hive_id]))

class AddNucleusQueenFormView(FormView):
	form_class = AddQueenForm
	template_name = 'add_nucleus_queen.html'

	def get_context_data(self, **kwargs):
		nucleus = Nucleus.objects.filter(nucleus_id__contains=self.kwargs['nucleus'])
		kwargs['nucleus'] = nucleus[0]
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		nucleus = Nucleus.objects.filter(nucleus_id__contains=self.kwargs['nucleus'])

		nucleus_queen_data = NucleusQueen(
			queen_name=form.cleaned_data['queen_name'],
			queen_added_date=form.cleaned_data['queen_added_date'],
			queen_removed_date=form.cleaned_data['queen_removed_date'],
			nucleus_id=nucleus[0],
		)
		nucleus_queen_data.save()
		return HttpResponseRedirect(reverse('nucleus', args=[nucleus[0].nucleus_id]))

class AddNoteFormView(FormView):
	form_class = AddNoteForm
	template_name = 'add_note.html'

	def get_context_data(self, **kwargs):
		hive = Hive.objects.filter(hive_id__contains=self.kwargs['hive'])
		kwargs['hive'] = hive[0]
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		hive = Hive.objects.filter(hive_id__contains=self.kwargs['hive'])

		note_data = Note(
			text=form.cleaned_data['text'],
			hive_id=hive[0],
		)
		note_data.save()
		return HttpResponseRedirect(reverse('notes', args=[hive[0].hive_id]))

class DeleteLocationView(DeleteView):
	model = Location
	template_name = 'delete_location.html'
	
	def get_success_url(self):
		return '{}'.format(reverse('index'))

class DeleteHiveView(DeleteView):
	model = Hive
	template_name = 'delete_hive.html'

	def get_context_data(self, **kwargs):
		context = {}
		if self.object:
			context['object'] = self.object
			context_object_name = self.get_context_object_name(self.object)
			if context_object_name:
				context[context_object_name] = self.object
		context.update(kwargs)
		return super().get_context_data(**context)

	def get_success_url(self):
		try:
			return '{}'.format(reverse('location', args=[self.object.__dict__['location_id_id']]))
		except Exception as e:
			raise ImproperlyConfigured('No URL to redirect to. Provide a success_url.')

class DeleteCheckView(DeleteView):
	model = Check
	template_name = 'delete_check.html'

	def get_context_data(self, **kwargs):
		context = {}
		if self.object:
			context['object'] = self.object
			context_object_name = self.get_context_object_name(self.object)
			if context_object_name:
				context[context_object_name] = self.object
		context.update(kwargs)
		return super().get_context_data(**context)

	def get_success_url(self):
		try:
			return '{}'.format(reverse('hive', args=[self.object.__dict__['hive_id_id']]))
		except Exception as e:
			raise ImproperlyConfigured('No URL to redirect to. Provide a success_url.')

class DeleteQueenView(DeleteView):
	model = Queen
	template_name = 'delete_queen.html'

	def get_context_data(self, **kwargs):
		context = {}
		if self.object:
			context['object'] = self.object
			context_object_name = self.get_context_object_name(self.object)
			if context_object_name:
				context[context_object_name] = self.object
		context.update(kwargs)
		return super().get_context_data(**context)

	def get_success_url(self):
		try:
			return '{}'.format(reverse('hive', args=[self.object.__dict__['hive_id_id']]))
		except Exception as e:
			raise ImproperlyConfigured('No URL to redirect to. Provide a success_url.')

class DeleteNucleusQueenView(DeleteView):
	model = NucleusQueen
	template_name = 'delete_queen.html'

	def get_context_data(self, **kwargs):
		context = {}
		if self.object:
			context['object'] = self.object
			context_object_name = self.get_context_object_name(self.object)
			if context_object_name:
				context[context_object_name] = self.object
		context.update(kwargs)
		return super().get_context_data(**context)

	def get_success_url(self):
		try:
			return '{}'.format(reverse('nucleus', args=[self.object.__dict__['nucleus_id_id']]))
		except Exception as e:
			raise ImproperlyConfigured('No URL to redirect to. Provide a success_url.')

class DeleteNoteView(DeleteView):
	model = Note
	template_name = 'delete_note.html'

	def get_context_data(self, **kwargs):
		context = {}
		if self.object:
			context['object'] = self.object
			context_object_name = self.get_context_object_name(self.object)
			if context_object_name:
				context[context_object_name] = self.object
		context.update(kwargs)
		return super().get_context_data(**context)

	def get_success_url(self):
		try:
			return '{}'.format(reverse('notes', args=[self.object.__dict__['hive_id_id']]))
		except Exception as e:
			raise ImproperlyConfigured('No URL to redirect to. Provide a success_url.')


class UpdateLocationView(UpdateView):
	model = Location
	template_name = 'update_location.html'
	fields = ['location_name']

	def get_success_url(self):
		return reverse('location', args=[self.kwargs['pk']])

class UpdateHiveView(UpdateView):
	model = Hive
	template_name = 'update_hive.html'
	fields = ['hive_number']

	def get_success_url(self):
		return reverse('hive', args=[self.kwargs['pk']])

class UpdateCheckView(UpdateView):
	model = Check
	template_name = 'update_check.html'
	fields = ['created_on', 'opened_honey', 'closed_honey', 'opened_brood', 'closed_brood', 'drone_cell', 'queen_cell', 'pollen_cell', 'observation']

	def get_form(self):
		form = super().get_form()
		form.fields['created_on'].widget = DatePickerInput()
		return form

	def get_success_url(self):
		return reverse('check', args=[self.kwargs['pk']])
		
class UpdateQueenView(UpdateView):
	model = Queen
	template_name = 'update_queen.html'
	fields = ['queen_name', 'queen_added_date', 'queen_removed_date']

	def get_success_url(self):
		return reverse('queen', args=[self.kwargs['pk']])

class HiveChartView(TemplateView):
	model = Hive
	template_name = 'hive_chart.html'

	def get_context_data(self, **kwargs):
		context = super(HiveChartView, self).get_context_data(**kwargs)
		data = Check.objects.filter(hive_id=kwargs['hive']).order_by('created_on')
		hive_num = Hive.objects.get(hive_id=kwargs['hive']).hive_number

		labels = []
		for i in data:
			labels.append(i)

		context['hive_num'] = hive_num
		context['data'] = data
		context['labels'] = labels

		if len(data) >= 2:
			data_len = len(data) - 2
			diff = data[data_len:]

			result = {}

			result['opened_honey'] = diff[1].opened_honey - diff[0].opened_honey
			result['closed_honey'] = diff[1].closed_honey - diff[0].closed_honey
			result['opened_brood'] = diff[1].opened_brood - diff[0].opened_brood
			result['closed_brood'] = diff[1].closed_brood - diff[0].closed_brood
			result['drone_cell'] = diff[1].drone_cell - diff[0].drone_cell
			result['queen_cell'] = diff[1].queen_cell - diff[0].queen_cell
			result['pollen_cell'] = diff[1].pollen_cell - diff[0].pollen_cell
			
			context['result'] = result
		return context

class UpdateNoteView(UpdateView):
	model = Note
	template_name = 'update_note.html'
	fields = ['text']

	def get_context_data(self, **kwargs):
		context = {}
		if self.object:
			context['object'] = self.object
			context_object_name = self.get_context_object_name(self.object)
			if context_object_name:
				context[context_object_name] = self.object
		context.update(kwargs)
		return super().get_context_data(**context)

	def get_success_url(self):
		return reverse('notes', args=[self.object.__dict__['hive_id_id']])