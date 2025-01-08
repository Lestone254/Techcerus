from django.db import models
from django.utils import timezone

# Create your models here.
class userMsg(models.Model):
  userName = models.CharField(max_length=255)
  telNumber = models.IntegerField()
  userEmail = models.EmailField(max_length=255)
  msgHeading = models.CharField(max_length=70)
  msgBody = models.TextField(max_length=100)

class freeQuote(models.Model):
  userQuoteName = models.CharField(max_length=255)
  telQuoteNumber = models.IntegerField()
  userQuoteEmail = models.EmailField(max_length=255)
  serviceQuoteCategory = models.CharField(max_length=255)
  msgQuoteHeading = models.CharField(max_length=70)
  msgQuoteBody = models.TextField(max_length=100)

class projectPost(models.Model):
  projectImg = models.ImageField(upload_to='static/assets/images')
  projectName = models.CharField(max_length=100)
  projectDescription = models.CharField(max_length=255)
  projectFeatures = models.CharField(max_length=100)
  projectLanguages = models.CharField(max_length=50)

class clientTestimonials(models.Model):
  testimonialLogo = models.ImageField(upload_to='static/assets/images')
  testimonialStatement = models.TextField(max_length=100)
  testimonialImage = models.ImageField(upload_to='static/assets/images')
  testimonialName = models.CharField(max_length=50)
  testimonialTitle = models.CharField(max_length=50)

class blogPosts(models.Model):
  blogImg = models.ImageField(upload_to='static/assets/images')
  blogUserImg = models.ImageField(upload_to='static/assets/images')
  blogAuthor = models.CharField(max_length=50)
  blogTitle = models.CharField(max_length=30)
  blogRead = models.TextField(max_length=1000)
  timestamp = models.DateTimeField(default=timezone.now, editable=False)

class userServices(models.Model):
  userName = models.CharField(max_length=255)
  telNumber = models.IntegerField()
  userEmail = models.EmailField(max_length=255)
  msgHeading = models.CharField(max_length=70)
  msgBody = models.TextField(max_length=100)
