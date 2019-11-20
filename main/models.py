from django.db import models #every model inherits from this
from datetime import datetime

# a model is represented by a table in the db(.sqlite3)
# each field in the model is a column in the table
# makemigrations, migrate
class Water(models.Model):
	water_title = models.CharField(max_length=200, default="Upcoming Watering")
	water_time = models.DateTimeField("Date and Time", default=datetime.now())
	water_duration = models.DurationField() #duration in seconds

	def __str__(self):
		return self.water_title

