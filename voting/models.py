from django.db import models

# Create your models here.

class Feedback(models.Model):
     feedback_name=models.CharField(max_length=50)
     feedback_phone=models.CharField(max_length=20)
     feedback_email=models.CharField(max_length=50)
     feedback_address=models.CharField(max_length=100)
     feedback_query=models.CharField(max_length=500)
     
class Contact(models.Model):
     contact_name=models.CharField(max_length=50)
     contact_phone=models.CharField(max_length=20)
     contact_email=models.CharField(max_length=50)
     contact_address=models.CharField(max_length=100)
     contact_query=models.CharField(max_length=500)     
     
class Registration(models.Model):
     GENDER_CHOICE = (('Male','Male'),('Female','Female'))
     phone=models.CharField(max_length=20)
     gender=models.CharField(max_length=7,choices=GENDER_CHOICE)
     voter_id=models.CharField(max_length=50)
     address=models.CharField(max_length=100)
     state=models.CharField(max_length=500)          
     country=models.CharField(max_length=500)          
     copy=models.CharField(max_length=500)          
     
class Candidate(models.Model):
     candidate_name=models.CharField(max_length=50)
     party=models.CharField(max_length=20)
     area=models.CharField(max_length=50)
     candidate_address=models.CharField(max_length=100)
     candidate_query=models.CharField(max_length=500)     
     candidate_photo=models.CharField(max_length=500) 

class News(models.Model):
     news_link=models.CharField(max_length=200)     
     news_text=models.CharField(max_length=1000)     
          