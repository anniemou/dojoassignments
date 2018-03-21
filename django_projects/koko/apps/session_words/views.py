 # -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'word_list' not in request.session:
        request.session['word_list'] = []
    return render(request, "session_words/index.html")

def process(request):
    word = {
        'word': request.POST['word'],
        'color': request.POST['color'],
        'bold': request.POST.get('bold', '')
    }
    request.session['word_list'].append(word)

    return redirect('/session_words/')

def clear(request):
    request.session.clear()
    return redirect('/session_words/')

