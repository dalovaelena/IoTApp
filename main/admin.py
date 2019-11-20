from django.contrib import admin
from .models import Water

#Register models

class WaterAdmin(admin.ModelAdmin):
	""" #change order of fields
	fields = ["water_time",
			"water_title",
			"water_duration"]"""

	#group fiels into sets (useful if there are many)
	fieldsets = [
		("Title/date", {"fields": ["water_title", "water_time"]}),
		("Content", {"fields": ["water_duration"]})
	]

#admin.site.register(Tutorial)
admin.site.register(Water, WaterAdmin)