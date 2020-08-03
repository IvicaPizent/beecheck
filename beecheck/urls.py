from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('location/<int:location>/', views.location, name='location'),
	path('hive/<int:hive>/', views.hive, name='hive'),
	path('hive_chart/<int:hive>/', views.HiveChartView.as_view(), name='hive_chart'),
	path('nucleus/<int:nucleus>/', views.nucleus, name='nucleus'),
	path('check/<int:check>/', views.check, name='check'),
	path('nucleus_check/<int:nucleus_check>/', views.nucleus_check, name='nucleus_check'),
	path('queen/<int:queen>/', views.queen, name='queen'),
	path('nucleus_queen/<int:nucleus_queen>/', views.nucleus_queen, name='nucleus_queen'),
	path('notes/<int:notes>/', views.notes, name='notes'),

	path('add_location/', views.AddLocationFormView.as_view(), name='add_location'),
	path('add_hive/<int:location>/', views.AddHiveFormView.as_view(), name='add_hive'),
	path('add_nucleus/<int:location>/', views.AddNucleusFormView.as_view(), name='add_nucleus'),
	path('add_check/<int:hive>/', views.AddCheckFormView.as_view(), name='add_check'),
	path('add_nucleus_check/<int:nucleus>/', views.AddNucleusCheckFormView.as_view(), name='add_nucleus_check'),
	path('add_queen/<int:hive>/', views.AddQueenFormView.as_view(), name='add_queen'),
	path('add_nucleus_queen/<int:nucleus>/', views.AddNucleusQueenFormView.as_view(), name='add_nucleus_queen'),
	path('add_note/<int:hive>/', views.AddNoteFormView.as_view(), name='add_note'),

	path('delete_location/<int:pk>/', views.DeleteLocationView.as_view(), name='delete_location'),
	path('delete_hive/<int:pk>/', views.DeleteHiveView.as_view(), name='delete_hive'),
	path('delete_check/<int:pk>/', views.DeleteCheckView.as_view(), name='delete_check'),
	path('delete_queen/<int:pk>/', views.DeleteQueenView.as_view(), name='delete_queen'),
	path('delete_nucleus_queen/<int:pk>/', views.DeleteNucleusQueenView.as_view(), name='delete_nucleus_queen'),
	path('delete_note/<int:pk>/', views.DeleteNoteView.as_view(), name='delete_note'),

	path('update_location/<int:pk>/', views.UpdateLocationView.as_view(), name='update_location'),
	path('update_hive/<int:pk>/', views.UpdateHiveView.as_view(), name='update_hive'),
	path('update_check/<int:pk>/', views.UpdateCheckView.as_view(), name='update_check'),
	path('update_queen/<int:pk>/', views.UpdateQueenView.as_view(), name='update_queen'),
	path('update_note/<int:pk>/', views.UpdateNoteView.as_view(), name='update_note'),
]