from django.db import models

class Stat(models.Model):
    RunningBack = models.CharField(max_length=255)

    def __str__(self):
        return self.RunningBack

class Yard(models.Model):
    Receiver = models.CharField(max_length=255)

    def __str__(self):
        return self.Receiver

class Location(models.Model):
    City = models.CharField(max_length=255)

    def __str__(self):
        return self.City

class Running_Back(models.Model):
    Back = models.CharField(max_length=255)

    def __str__(self):
        return self.Back

class Quarter_Back(models.Model):
    QB = models.CharField(max_length=255)

    def __str__(self):
        return self.QB











