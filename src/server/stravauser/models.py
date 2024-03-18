from django.contrib.auth.models import User
from django.db import models

class Athlete(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='athlete')
    # data from strava
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)
    resource_state = models.IntegerField()
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], blank=True, null=True)
    premium = models.BooleanField(default=False)
    summit = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    badge_type_id = models.IntegerField()
    weight = models.FloatField(blank=True, null=True)
    profile_medium = models.URLField()
    profile = models.URLField()
    friend = models.BooleanField(default=False, null=True)  # Assuming boolean, adjust if different
    follower = models.BooleanField(default=False, null=True)  # Assuming boolean, adjust if different

class TokenData(models.Model):
    token_type = models.CharField(max_length=10)
    expires_at = models.IntegerField()
    expires_in = models.IntegerField()
    refresh_token = models.CharField(max_length=100)
    access_token = models.CharField(max_length=100)
    athlete = models.OneToOneField(Athlete, on_delete=models.CASCADE)
