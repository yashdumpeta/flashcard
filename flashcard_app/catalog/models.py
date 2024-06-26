from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Deck(models.Model):
    deck_name = models.CharField(blank=False, max_length=100, help_text="Enter name of deck")
    description = models.TextField(blank=True, max_length=200, help_text="Give a description for this deck...")
    time_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__ (self):
        return self.deck_name, self.user

    def get_absolute_url(self):
        """Returns the url to access a particular genre instance."""
        return reverse('deck-detail', args=[str(self.id)])
    
    
    pass

class Card(models.Model):
    #the deck, will delete the related objects when the reference object is deleted
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='cards') 
    # when the card is created, auto sets the field to current date and time when object is created
    created_at = models.DateTimeField(auto_now_add=True) 
    # when the card is updated, auto sets the field to current date and time when object is updated
    updated_at = models.DateTimeField(auto_now=True)
    #front, the question user wants to answer
    front_side = models.TextField()
    #back, the answer to the front side
    back_side = models.TextField()
    
    
    
    