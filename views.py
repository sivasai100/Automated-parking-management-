from django.shortcuts import render, redirect
from .models import ParkingSlot, Booking
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def home(request):
    return render(request, 'home.html')

@login_required
def available_slots(request):
    slots = ParkingSlot.objects.filter(is_available=True)
    return render(request, 'parking/available_slots.html', {'slots': slots})

@login_required
def book_slot(request, slot_id):
    slot = ParkingSlot.objects.get(id=slot_id)
    if slot.is_available:
        booking = Booking.objects.create(user=request.user, slot=slot)
        slot.is_available = False
        slot.save()
    return redirect('my_bookings')

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'parking/my_bookings.html', {'bookings': bookings})
