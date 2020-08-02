from django.test import TestCase

from datetime import date

from beecheck.models import Location, Hive, Nucleus, Check, NucleusCheck, Queen, NucleusQueen

class LocationModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		Location.objects.create(location_name='Dummy')

	def test_location_name_label(self):
		location = Location.objects.get(location_id=1)
		field_label = location._meta.get_field('location_name').verbose_name
		self.assertEqual(field_label, 'location name')

	def test_location_name_max_length(self):
		location = Location.objects.get(location_id=1)
		max_length = location._meta.get_field('location_name').max_length
		self.assertEqual(max_length, 100)

	def test_location_name_is_location_name(self):
		location = Location.objects.get(location_id=1)
		expected_location_name = f'{location.location_name}'
		self.assertEqual(expected_location_name, str(location))

	def test_get_absolute_url(self):
		location = Location.objects.get(location_id=1)
		self.assertEqual(location.get_absolute_url(), '/beecheck/location/1/')

class HiveModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		location = Location.objects.create(location_name='Dummy')
		Hive.objects.create(hive_number='1', location_id=location)

	def test_hive_location_id(self):
		location = Location.objects.get(location_id=1)
		hive = Hive.objects.get(hive_id=1)
		self.assertEqual(hive.location_id.pk, location.location_id)

	def test_hive_number_label(self):
		hive = Hive.objects.get(hive_id=1)
		field_label = hive._meta.get_field('hive_number').verbose_name
		self.assertEqual(field_label, 'hive number')

	def test_hive_number_is_hive_number(self):
		hive = Hive.objects.get(hive_id=1)
		expected_hive_number = f'{hive.hive_number}'
		self.assertEqual(expected_hive_number, str(hive))

	def test_get_absolute_url(self):
		hive = Hive.objects.get(hive_id=1)
		self.assertEqual(hive.get_absolute_url(), '/beecheck/hive/1/')

class NucleusModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		location = Location.objects.create(location_name='Dummy')
		nucleus = Nucleus.objects.create(nucleus_number='1', location_id=location)

	def test_nucleus_location_id(self):
		location = Location.objects.get(location_id=1)
		nucleus = Nucleus.objects.get(nucleus_id=1)
		self.assertEqual(nucleus.location_id.pk, location.location_id)

	def test_nucleus_number_label(self):
		nucleus = Nucleus.objects.get(nucleus_id=1)
		field_label = nucleus._meta.get_field('nucleus_number').verbose_name
		self.assertEqual(field_label, 'nucleus number')

	def test_nucleus_number_is_nucleus_number(self):
		nucleus = Nucleus.objects.get(nucleus_id=1)
		expected_nucleus_number = f'{nucleus.nucleus_number}'
		self.assertEqual(expected_nucleus_number, str(nucleus))

	def test_get_absolute_url(self):
		nucleus = Nucleus.objects.get(nucleus_id=1)
		self.assertEqual(nucleus.get_absolute_url(), '/beecheck/nucleus/1/')

class CheckModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		location = Location.objects.create(location_name='Dummy')
		hive = Hive.objects.create(hive_number='1', location_id=location)
		Check.objects.create(created_on=date(2020, 7, 26), opened_honey='1', closed_honey='1',
									 opened_brood='1', closed_brood='1', drone_cell='1',
									 queen_cell='1', pollen_cell='1', observation='a',
									 hive_id=hive)

	def test_check_hive_id(self):
		hive = Hive.objects.get(hive_id=1)
		check = Check.objects.get(check_id=1)
		self.assertEqual(check.hive_id.pk, hive.hive_id)

	def test_opened_honey_label(self):
		check = Check.objects.get(check_id=1)
		field_label = check._meta.get_field('opened_honey').verbose_name
		self.assertEqual(field_label, 'opened honey')

	def test_opened_honey_max_digits(self):
		check = Check.objects.get(check_id=1)
		max_digits = check._meta.get_field('opened_honey').max_digits
		self.assertEqual(max_digits, 5)

	def test_opened_honey_decimal_places(self):
		check = Check.objects.get(check_id=1)
		decimal_places = check._meta.get_field('opened_honey').decimal_places
		self.assertEqual(decimal_places, 3)

	def test_closed_honey_label(self):
		check = Check.objects.get(check_id=1)
		field_label = check._meta.get_field('closed_honey').verbose_name
		self.assertEqual(field_label, 'closed honey')

	def test_closed_honey_max_digits(self):
		check = Check.objects.get(check_id=1)
		max_digits = check._meta.get_field('closed_honey').max_digits
		self.assertEqual(max_digits, 5)

	def test_closed_honey_decimal_places(self):
		check = Check.objects.get(check_id=1)
		decimal_places = check._meta.get_field('closed_honey').decimal_places
		self.assertEqual(decimal_places, 3)

	def test_opened_brood_label(self):
		check = Check.objects.get(check_id=1)
		field_label = check._meta.get_field('opened_brood').verbose_name
		self.assertEqual(field_label, 'opened brood')

	def test_opened_brood_max_digits(self):
		check = Check.objects.get(check_id=1)
		max_digits = check._meta.get_field('opened_brood').max_digits
		self.assertEqual(max_digits, 5)

	def test_opened_brood_decimal_places(self):
		check = Check.objects.get(check_id=1)
		decimal_places = check._meta.get_field('opened_brood').decimal_places
		self.assertEqual(decimal_places, 3)

	def test_closed_brood_label(self):
		check = Check.objects.get(check_id=1)
		field_label = check._meta.get_field('closed_brood').verbose_name
		self.assertEqual(field_label, 'closed brood')

	def test_closed_brood_max_digits(self):
		check = Check.objects.get(check_id=1)
		max_digits = check._meta.get_field('closed_brood').max_digits
		self.assertEqual(max_digits, 5)

	def test_closed_brood_decimal_places(self):
		check = Check.objects.get(check_id=1)
		decimal_places = check._meta.get_field('closed_brood').decimal_places
		self.assertEqual(decimal_places, 3)

	def test_drone_cell_label(self):
		check = Check.objects.get(check_id=1)
		field_label = check._meta.get_field('drone_cell').verbose_name
		self.assertEqual(field_label, 'drone cell')

	def test_drone_cell_max_digits(self):
		check = Check.objects.get(check_id=1)
		max_digits = check._meta.get_field('drone_cell').max_digits
		self.assertEqual(max_digits, 5)

	def test_drone_cell_decimal_places(self):
		check = Check.objects.get(check_id=1)
		decimal_places = check._meta.get_field('drone_cell').decimal_places
		self.assertEqual(decimal_places, 3)

	def test_queen_cell_label(self):
		check = Check.objects.get(check_id=1)
		field_label = check._meta.get_field('queen_cell').verbose_name
		self.assertEqual(field_label, 'queen cell')

	def test_pollen_cell_label(self):
		check = Check.objects.get(check_id=1)
		field_label = check._meta.get_field('pollen_cell').verbose_name
		self.assertEqual(field_label, 'pollen cell')

	def test_pollen_cell_max_digits(self):
		check = Check.objects.get(check_id=1)
		max_digits = check._meta.get_field('pollen_cell').max_digits
		self.assertEqual(max_digits, 5)

	def test_pollen_cell_decimal_places(self):
		check = Check.objects.get(check_id=1)
		decimal_places = check._meta.get_field('pollen_cell').decimal_places
		self.assertEqual(decimal_places, 3)

	def test_observation_label(self):
		check = Check.objects.get(check_id=1)
		field_label = check._meta.get_field('observation').verbose_name
		self.assertEqual(field_label, 'observation')

	def test_observation_max_length(self):
		check = Check.objects.get(check_id=1)
		max_length = check._meta.get_field('observation').max_length
		self.assertEqual(max_length, 2000)

	def test_observation_blank(self):
		check = Check.objects.get(check_id=1)
		blank = check._meta.get_field('observation').blank
		self.assertTrue(blank)

	def test_created_on_is_created_on(self):
		check = Check.objects.get(check_id=1)
		expected_created_on = f'{check.created_on}'
		self.assertEqual(expected_created_on, str(check))

	def test_check_date_id_dd_mm_yyyy(self):
		check = Check.objects.get(check_id=1)
		expected_check_date = f"{check.created_on.strftime('%d.%m.%Y.')}"
		self.assertEqual(expected_check_date, check.check_date())

	def test_get_absolute_url(self):
		check = Check.objects.get(check_id=1)
		self.assertEqual(check.get_absolute_url(), '/beecheck/check/1/')

class NucleusCheckModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		location = Location.objects.create(location_name='Dummy')
		nucleus = Nucleus.objects.create(nucleus_number='1', location_id=location)
		NucleusCheck.objects.create(created_on=date(2020, 7, 26),
													observation='a', nucleus_id=nucleus)
	def test_nucleus_check_nucleus_id(self):
		nucleus = Nucleus.objects.get(nucleus_id=1)
		nucleus_check = NucleusCheck.objects.get(nucleus_check_id=1)
		self.assertEqual(nucleus_check.nucleus_id.pk, nucleus.nucleus_id)

	def test_observation_label(self):
		nucleus_check = NucleusCheck.objects.get(nucleus_check_id=1)
		field_label = nucleus_check._meta.get_field('observation').verbose_name
		self.assertEqual(field_label, 'observation')

	def test_observation_max_length(self):
		nucleus_check = NucleusCheck.objects.get(nucleus_check_id=1)
		max_length = nucleus_check._meta.get_field('observation').max_length
		self.assertEqual(max_length, 2000)

	def test_observation_blank(self):
		nucleus_check = NucleusCheck.objects.get(nucleus_check_id=1)
		blank = nucleus_check._meta.get_field('observation').blank
		self.assertTrue(blank)

	def test_created_on_is_created_on(self):
		nucleus_check = NucleusCheck.objects.get(nucleus_check_id=1)
		expected_created_on = f'{nucleus_check.created_on}'
		self.assertEqual(expected_created_on, str(nucleus_check))

	def test_get_absolute_url(self):
		nucleus_check = NucleusCheck.objects.get(nucleus_check_id=1)
		self.assertEqual(nucleus_check.get_absolute_url(), '/beecheck/nucleus_check/1/')

class QueenModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		location = Location.objects.create(location_name='Dummy')
		hive = Hive.objects.create(hive_number='1', location_id=location)
		Queen.objects.create(queen_name='Dummy', queen_added_date=date(2020,7, 26),
							 queen_removed_date=date(2022, 7, 26), hive_id=hive)

	def test_queen_hive_id(self):
		hive = Hive.objects.get(hive_id=1)
		queen = Queen.objects.get(queen_id=1)
		self.assertEqual(queen.hive_id.pk, hive.hive_id)

	def test_queen_name_label(self):
		queen = Queen.objects.get(queen_id=1)
		field_label = queen._meta.get_field('queen_name').verbose_name
		self.assertEqual(field_label, 'queen name')

	def test_queen_name_max_digits(self):
		queen = Queen.objects.get(queen_id=1)
		max_length = queen._meta.get_field('queen_name').max_length
		self.assertEqual(max_length, 100)

	def test_queen_removed_date_is_blank(self):
		queen = Queen.objects.get(queen_id=1)
		blank = queen._meta.get_field('queen_removed_date').blank
		self.assertTrue(blank)

	def test_queen_removed_date_is_null(self):
		queen = Queen.objects.get(queen_id=1)
		null = queen._meta.get_field('queen_removed_date').null
		self.assertTrue(null)

	def test_get_absolute_url(self):
		queen = Queen.objects.get(queen_id=1)
		self.assertEqual(queen.get_absolute_url(), '/beecheck/queen/1/')

class NucleusQueenModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		location = Location.objects.create(location_name='Dummy')
		nucleus = Nucleus.objects.create(nucleus_number='1', location_id=location)
		NucleusQueen.objects.create(queen_name='Dummy', queen_added_date=date(2020,7, 26),
							 queen_removed_date=date(2022, 7, 26), nucleus_id=nucleus)

	def test_nucleus_queen_hive_id(self):
		nucleus = Nucleus.objects.get(nucleus_id=1)
		nucleus_queen = NucleusQueen.objects.get(nucleus_queen_id=1)
		self.assertEqual(nucleus_queen.nucleus_id.pk, nucleus.nucleus_id)

	def test_nucleus_queen_name_label(self):
		nucleus_queen = NucleusQueen.objects.get(nucleus_queen_id=1)
		field_label = nucleus_queen._meta.get_field('queen_name').verbose_name
		self.assertEqual(field_label, 'queen name')

	def test_nucleus_queen_name_max_digits(self):
		nucleus_queen = NucleusQueen.objects.get(nucleus_queen_id=1)
		max_length = nucleus_queen._meta.get_field('queen_name').max_length
		self.assertEqual(max_length, 100)

	def test_nucleus_queen_removed_date_is_blank(self):
		nucleus_queen = NucleusQueen.objects.get(nucleus_queen_id=1)
		blank = nucleus_queen._meta.get_field('queen_removed_date').blank
		self.assertTrue(blank)

	def test_nucleus_queen_removed_date_is_null(self):
		nucleus_queen = NucleusQueen.objects.get(nucleus_queen_id=1)
		null = nucleus_queen._meta.get_field('queen_removed_date').null
		self.assertTrue(null)

	def test_get_absolute_url(self):
		nucleus_queen = NucleusQueen.objects.get(nucleus_queen_id=1)
		self.assertEqual(nucleus_queen.get_absolute_url(), '/beecheck/nucleus_queen/1/')
