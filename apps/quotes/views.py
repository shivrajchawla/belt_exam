# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

def index(request):
    if 'user_id' not in request.session:
        return render(request,'loginandregistration/index.html')
    else:
        me = User.objects.filter(id = request.session['user_id'])
        context = Quote.objects.all()
        user = User.objects.get(id = request.session['user_id'])
        liked_quotes = Quote.objects.filter(favorites = user)
        return render(request,'quotes/index.html',{"context": context,"liked_quotes": liked_quotes})

def add_quote(request):
    res = Quote.objects.valid_quote(request.POST)
    if res['status']:
        created_quote = Quote.objects.create_quote(request.POST)
        return redirect('/quotes/show_posts')   
    else:
        for error in res['errors']:
            messages.error(request,error)
        return redirect('/quotes/')

def like(request):
    res = Quote.objects.like(request.POST)
    if res['message'] == "Success!":
        return redirect('/quotes/show_posts')
    else:
        return redirect('/quotes/')

def show_your_posts(request):
    user = User.objects.get(id = request.session['user_id'])
    context = Quote.objects.filter(quote_posted_by = user)
    liked_quotes = Quote.objects.filter(favorites = user)
    count = Quote.objects.count()
    return render(request,'quotes/show_your_posts.html',{'context': context, "count": count, "liked_quotes": liked_quotes})




