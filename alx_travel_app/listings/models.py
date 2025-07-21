from django.db import models
from django.db import models
from django.utils import timezone


class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    customer_name = models.CharField(max_length=255)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.customer_name} booking at {self.listing.title}'


class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=255)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Review by {self.reviewer_name} on {self.listing.title}'


# Create your models here.
