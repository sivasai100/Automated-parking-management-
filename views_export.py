import csv
from django.http import HttpResponse
from .models import Booking

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="bookings.csv"'
    writer = csv.writer(response)
    writer.writerow(['User', 'Slot', 'Start', 'End', 'Price'])
    for b in Booking.objects.all():
        writer.writerow([b.user.username, b.slot.slot_number, b.start_time, b.end_time, b.price])
    return response
