from django.test import TestCase

from beecheck.forms import AddLocationForm, AddHiveForm, AddNucleusForm, AddCheckForm, AddNucleusCheckForm, AddQueenForm

class AddLocationFormTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.form = AddLocationForm()

	def test_location_name_field_label(self):
		self.assertTrue(self.form.fields['location_name'].label == None or self.form.fields['location_name'].label == 'location name')

	def test_location_name_field_max_length(self):
		self.assertTrue(self.form.fields['location_name'].max_length == 100)

class AddHiveFormTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.form = AddHiveForm()

	def test_hive_number_field_label(self):
		self.assertTrue(self.form.fields['hive_number'].label == None or self.form.fields['hive_number'].label == 'hive number')

class AddNucleusFormTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.form = AddNucleusForm()

	def test_nucleus_number_field_label(self):
		self.assertTrue(self.form.fields['nucleus_number'].label == None or self.form.fields['nucleus_number'].label == 'nucleus number')

class AddCheckFormTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.form = AddCheckForm()

	def test_created_on_field_input_formats(self):
		self.assertTrue(self.form.fields['created_on'].input_formats[0] == '%d/%m/%Y')

	def test_opened_honey_field_max_digits(self):
		self.assertEqual(self.form.fields['opened_honey'].max_digits, 5)

	def test_opened_honey_field_decimal_places(self):
		self.assertEqual(self.form.fields['opened_honey'].decimal_places, 3)

	def test_opened_honey_field_required(self):
		self.assertFalse(self.form.fields['opened_honey'].required)

	def test_closed_honey_field_max_digits(self):
		self.assertEqual(self.form.fields['closed_honey'].max_digits, 5)

	def test_closed_honey_field_decimal_places(self):
		self.assertEqual(self.form.fields['closed_honey'].decimal_places, 3)

	def test_closed_honey_field_required(self):
		self.assertFalse(self.form.fields['closed_honey'].required)

	def test_opened_brood_field_max_digits(self):
		self.assertEqual(self.form.fields['opened_brood'].max_digits, 5)

	def test_opened_brood_field_decimal_places(self):
		self.assertEqual(self.form.fields['opened_brood'].decimal_places, 3)

	def test_opened_brood_field_required(self):
		self.assertFalse(self.form.fields['opened_brood'].required)

	def test_closed_brood_field_max_digits(self):
		self.assertEqual(self.form.fields['closed_brood'].max_digits, 5)

	def test_closed_brood_field_decimal_places(self):
		self.assertEqual(self.form.fields['closed_brood'].decimal_places, 3)

	def test_closed_brood_field_required(self):
		self.assertFalse(self.form.fields['closed_brood'].required)

	def test_drone_cell_field_max_digits(self):
		self.assertEqual(self.form.fields['drone_cell'].max_digits, 5)

	def test_drone_cell_field_decimal_places(self):
		self.assertEqual(self.form.fields['drone_cell'].decimal_places, 3)

	def test_drone_cell_field_required(self):
		self.assertFalse(self.form.fields['drone_cell'].required)

	def test_queen_cell_field_required(self):
		self.assertFalse(self.form.fields['queen_cell'].required)

	def test_pollen_cell_field_max_digits(self):
		self.assertEqual(self.form.fields['pollen_cell'].max_digits, 5)

	def test_pollen_cell_field_decimal_places(self):
		self.assertEqual(self.form.fields['pollen_cell'].decimal_places, 3)

	def test_pollen_cell_field_required(self):
		self.assertFalse(self.form.fields['pollen_cell'].required)

	def test_observation_field_max_digits(self):
		self.assertEqual(self.form.fields['observation'].max_length, 2000)

	def test_observation_field_required(self):
		self.assertFalse(self.form.fields['observation'].required)

class AddNucleusCheckFormTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.form = AddNucleusCheckForm()

	def test_created_on_field_input_formats(self):
		self.assertTrue(self.form.fields['created_on'].input_formats[0] == '%d/%m/%Y')	

	def test_observation_field_max_digits(self):
		self.assertEqual(self.form.fields['observation'].max_length, 2000)

	def test_observation_field_required(self):
		self.assertFalse(self.form.fields['observation'].required)

class AddQueenFormTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.form = AddQueenForm()

	def test_queen_name_field_max_digits(self):
		self.assertEqual(self.form.fields['queen_name'].max_length, 100)

	def test_queen_added_date_field_input_formats(self):
		self.assertTrue(self.form.fields['queen_added_date'].input_formats[0] == '%d/%m/%Y')

	def test_queen_removed_date_field_input_formats(self):
		self.assertTrue(self.form.fields['queen_removed_date'].input_formats[0] == '%d/%m/%Y')

	def test_queen_removed_date_field_required(self):
		self.assertFalse(self.form.fields['queen_removed_date'].required)

