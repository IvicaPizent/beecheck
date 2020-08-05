from django.db import models
from django.urls import reverse

class Location(models.Model):
	location_id = models.AutoField(primary_key=True)
	location_name = models.CharField(max_length=100)
	created_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.location_name)

	def get_absolute_url(self):
		return reverse('location', args=[self.location_id])

class Hive(models.Model):
	hive_id = models.AutoField(primary_key=True)
	hive_number = models.IntegerField()
	created_on = models.DateTimeField(auto_now_add=True)
	location_id = models.ForeignKey(Location, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.hive_number)

	def get_absolute_url(self):
		return reverse('hive', args=[self.hive_id])

class Nucleus(models.Model):
	nucleus_id = models.AutoField(primary_key=True)
	nucleus_number = models.IntegerField()
	created_on = models.DateTimeField(auto_now_add=True)
	location_id = models.ForeignKey(Location, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.nucleus_number)

	def get_absolute_url(self):
		return reverse('nucleus', args=[self.nucleus_id])

class Check(models.Model):
	check_id = models.AutoField(primary_key=True)
	created_on = models.DateField()
	opened_honey = models.DecimalField(max_digits=5, decimal_places=3)
	closed_honey = models.DecimalField(max_digits=5, decimal_places=3)
	opened_brood = models.DecimalField(max_digits=5, decimal_places=3)
	closed_brood = models.DecimalField(max_digits=5, decimal_places=3)
	drone_cell = models.DecimalField(max_digits=5, decimal_places=3)
	queen_cell = models.IntegerField()
	pollen_cell = models.DecimalField(max_digits=5, decimal_places=3)
	observation = models.CharField(max_length=2000, blank=True)
	hive_id = models.ForeignKey(Hive, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.created_on)

	def check_date(self):
		return str(self.created_on.strftime('%d.%m.%Y.'))

	def get_absolute_url(self):
		return reverse('check', args=[self.check_id])

class NucleusCheck(models.Model):
	nucleus_check_id = models.AutoField(primary_key=True)
	created_on = models.DateField()
	observation = models.CharField(max_length=2000, blank=True)
	nucleus_id = models.ForeignKey(Nucleus, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.created_on)

	def get_absolute_url(self):
		return reverse('nucleus_check', args=[self.nucleus_check_id])

class Queen(models.Model):
	queen_id = models.AutoField(primary_key=True)
	queen_name = models.CharField(max_length=100)
	queen_added_date = models.DateField()
	queen_removed_date = models.DateField(blank=True, null=True)
	hive_id = models.ForeignKey(Hive, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.queen_name)

	def get_absolute_url(self):
		return reverse('queen', args=[self.queen_id])

class NucleusQueen(models.Model):
	nucleus_queen_id = models.AutoField(primary_key=True)
	queen_name = models.CharField(max_length=100)
	queen_added_date = models.DateField()
	queen_removed_date = models.DateField(blank=True, null=True)
	nucleus_id = models.ForeignKey(Nucleus, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.queen_name)

	def get_absolute_url(self):
		return reverse('nucleus_queen', args=[self.nucleus_queen_id])

'''class Note(models.Model):
	note_id = models.AutoField(primary_key=True)
	created_on = models.DateTimeField(auto_now_add=True)
	text = models.CharField(max_length=2000, blank=True)
	location_id = models.ForeignKey(Location, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.created_on.strftime('%d.%m.%Y.'))

	def get_absolute_url(self):
		return reverse('notes', args=[self.note_id])'''


	
	