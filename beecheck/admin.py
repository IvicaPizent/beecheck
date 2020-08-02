from django.contrib import admin
from .models import Location, Hive, Nucleus, Check, NucleusCheck, Queen, NucleusQueen

admin.site.register(Location)
admin.site.register(Hive)
admin.site.register(Nucleus)
admin.site.register(Check)
admin.site.register(NucleusCheck)
admin.site.register(Queen)
admin.site.register(NucleusQueen)
