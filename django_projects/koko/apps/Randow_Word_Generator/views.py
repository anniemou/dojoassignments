# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
def index(request):
    if 'attempts' in request.session:
        request.session['attempts'] += 1
    else:
        request.session['attempts'] = 1

    rndstring = get_random_string(length=14)
    context = { "rndstring" : rndstring }
    return render(request,'Randow_Word_Generator/index.html', context)

def reset(request):
    request.session['attempts'] = 0
    return redirect('/random_word')

