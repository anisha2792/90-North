from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .models import ChatMessage
from django.contrib.auth.decorators import login_required

def signup(request):
         if request.method == 'POST':
             username, password = request.POST['username'], request.POST['password']
             User.objects.create_user(username=username, password=password)
             return redirect('login')
         return render(request, 'signup.html')

def user_login(request):
         if request.method == 'POST':
             user = authenticate(username=request.POST['username'], password=request.POST['password'])
             if user:
                 login(request, user)
                 return redirect('chat')
         return render(request, 'login.html')

def user_logout(request):
         logout(request)
         return redirect('login')

@login_required
def chat(request):
         users = User.objects.exclude(id=request.user.id)
         return render(request, 'chat.html', {'users': users})
<form method="post">{% csrf_token %}
<input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Sign Up</button>
</form>
<form method="post">{% csrf_token %}
<input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">Log In</button>
</form>