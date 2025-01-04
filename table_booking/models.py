import datetime
from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

TIME_SLOTS = (
        ('12pm-2pm','12pm-2pm'),
        ('1pm-3pm','1pm-3pm'),
        ('2pm-4pm','2pm-4pm'),
        ('3pm-5pm','3pm-5pm'),
        ('4pm-6pm','4pm-6pm'),
        ('5pm-7pm','5pm-7pm'),
        
)

TABLE_TYPE = (
        ('1', 'A small and cosy table, with enough room for two, coffees and games'),
        ('2', 'A slightly larger table, with plenty of room for coffees, cakes and games - suitable for about 2-3 players'),
        ('3', 'A purpose built gaming table with a great deal of room for those lucky/unlucky rolls!'),
        ('4', 'A huge gaming table with hidden drawers for cards and areas to roll dice seen or unseen!')
)

class Booking(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        table_type = models.CharField(choices=TABLE_TYPE, default='1')
        booking_date = models.DateField(default=datetime.date.today)
        time = models.CharField(choices=TIME_SLOTS, default='8:00-9:00')
        num_of_guests = models.PositiveIntegerField(default=1, validators=[
                MaxValueValidator(12),
                MinValueValidator(1)
                ])
        booked_on = models.DateTimeField(auto_now_add=True)
        additional_message = models.TextField(max_length=300, null=True, blank=True)
        slug = AutoSlugField(max_length=70, unique=True, null=True)

        class Meta:
                ordering = ["-booked_on"]
        
        def __str__(self):
                return f'Booked by {self.user} for {self.num_of_guests} people at {self.time} on {self.booking_date}'

class UserProfile(models.Model):

        user = models.OneToOneField(User, on_delete=models.CASCADE)
        first_name = models.CharField(null=True, max_length=50)
        last_name = models.CharField(null=True, max_length=50)
        email = models.EmailField(max_length=300)
        favourite_game = models.CharField(null=True, max_length=100)

        def __str__(self):
                if self.user:
                        return self.email
