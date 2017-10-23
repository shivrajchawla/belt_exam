# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..loginandregistration.models import User
from django.db import models

class QuoteManager(models.Manager):
    def valid_quote(self,post):
        quoted_by = post['quoted_by']
        message = post['message']
        errors = []

        if len(quoted_by) < 3:
            errors.append("Quoted by must be more than 3 char")
        
        if len(message) < 10:
            errors.append("Type more than 10char for the message")

        return {'status': len(errors) == 0, 'errors': errors}    
    
    def create_quote(self,post):
        quoted_by = post['quoted_by']
        message = post['message']
        user_id = post['user_id']
        user = User.objects.get(id = user_id)
        self.create(quote_text = message, quote_author = quoted_by, quote_posted_by = user)
        data = {
            "shit" : self.get(quote_text = message)
        }
        return data
    
    def like(self,post):
        quote_id = post['like']
        user_id = post['user_id']
        user = User.objects.get(id=user_id) 
        quote = Quote.objects.get(id=quote_id)
        quote.favorites.add(user)
        data = {
            "message": "Success!"
        }
        return data
        


class Quote(models.Model):
    quote_text = models.TextField()
    quote_author = models.CharField(max_length=255)
    quote_posted_by = models.ForeignKey(User, related_name="posting_users")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    favorites = models.ManyToManyField(User, related_name = "favorite_quotes")
    objects = QuoteManager()
    def __str__(self):
        return "{} {} {} {} {} {}".format(self.quote_text,self.quote_author,self.quote_posted_by,self.created_at,self.updated_at,self.favorites)
    