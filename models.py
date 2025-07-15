from django.db import models
from django.contrib.auth.models import User

class ParkingSlot(models.Model):
    slot_number = models.CharField(max_length=10, unique=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.slot_number

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    price = models.FloatField(default=0.0)

    def calculate_price(self):
        if self.end_time:
            duration = self.end_time - self.start_time
            hours = duration.total_seconds() / 3600
            return round(hours * 10, 2)
        return 0.0
