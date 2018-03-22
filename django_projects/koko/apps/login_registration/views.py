# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import User
import bcrypt

# Create your views here.

def index(request):
    request.session.clear()
    return render(request, "login_registration/index.html")

def success(request):
    return render(request, "login_registration/success.html")

def register(request):
    email = request.POST['email']

    # O xrhsths
    user = User()

    if len(User.objects.filter(email = email)) > 0:
        print "O xrhsths yparxei hdh"
        return redirect("/login/")

    # Diabazw to password kryptografimeno
    request.session['message'] = "registered"
    hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    
    # Ftianxw ton xristi kai ton swzw
    user.firstname = request.POST['firstname']
    user.lastname = request.POST['lastname']
    user.email = email
    user.password = hashed
    user.save()

    # Dinw to firstname gia na doulepsei h success.html
    request.session['firstname'] = user.firstname

    return redirect("/login/success")

def login(request):
    email = request.POST['email']
    password = request.POST['password']

    user = User.objects.get(email = email)

    if bcrypt.checkpw(password.encode(), user.password.encode()):
        request.session['message'] = "logged in"
        
        # Dinw to firstname gia na doulepsei h success.html
        request.session['firstname'] = user.firstname
        return redirect("/login/success")

    return redirect("/login/")

    