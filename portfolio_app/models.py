from django.db import models

# Site-wide settings for colors & resume
class SiteSettings(models.Model):
    primary_color = models.CharField(max_length=7, default='#007bff', help_text="Hex code e.g. #ff0000")
    secondary_color = models.CharField(max_length=7, default='#6c757d')
    resume = models.FileField(upload_to='resumes/')
    def __str__(self): return "Site Settings"

# Introduction / Profile
class Profile(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    tagline = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)

# Education entries
class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_year = models.PositiveSmallIntegerField()
    end_year = models.PositiveSmallIntegerField(blank=True, null=True)
    details = models.TextField(blank=True)

# Soft skills
class SoftSkill(models.Model):
    name = models.CharField(max_length=50)

# Technical skills
class TechSkill(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.PositiveSmallIntegerField(default=75, help_text="Percentage")

# Projects
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True)
    completed_date = models.DateField()

# Certifications
class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    date_obtained = models.DateField()
    credential_url = models.URLField(blank=True)