"""
Copyright (c) 2024 KouroshAsli
All rights reserved.

This project is the intellectual property of KouroshAsli.
Unauthorized copying, modification, distribution, or use of this project,
via any medium, is strictly prohibited.

Contact: kouroshasli@proton.me
Telegram: @kouroshasli
GitHub: https://github.com/kouroshasli/TK
"""

from django.shortcuts import render
from django.views.generic import TemplateView

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def projects(request):
    return render(request, 'main/projects.html')

def contact(request):
    return render(request, 'main/contact.html') 