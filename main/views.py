from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

def home(request):
    return render(request, 'main/home.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            # Handle login error
            return render(request, 'main/login.html', {'error': 'Invalid login credentials'})
    return render(request, 'main/login.html')

def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        location = request.POST.get('location')
        phone_number = request.POST.get('phone_number')
        take_personality_test = request.POST.get('take_personality_test') == 'on'
        semester = int(request.POST.get('semester'))
        branch = request.POST.get('branch')

        # Perform registration logic
        name_parts = full_name.split()
        if len(name_parts) > 1:
            first_name = name_parts[0]
            last_name = ' '.join(name_parts[1:])
        else:
            first_name = full_name
            last_name = ''

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender,
            location=location,
            phone_number=phone_number,
            take_personality_test=take_personality_test,
            semester=semester,
            branch=branch
        )
        login(request, user)
        return redirect('dashboard')

    return render(request, 'main/register.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'main/dashboard.html')
    else:
        return redirect('home')

def features(request):
    return render(request, 'main/features.html')

def confession_matching(request):
    return render(request, 'main/confession_matching.html')

def compatibility_suggestions(request):
    return render(request, 'main/compatibility_suggestions.html')

def location_suggestions(request):
    return render(request, 'main/location_suggestions.html')

def update_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.date_of_birth = request.POST.get('date_of_birth')
        user.gender = request.POST.get('gender')
        user.location = request.POST.get('location')
        user.phone_number = request.POST.get('phone_number')
        user.semester = int(request.POST.get('semester'))
        user.branch = request.POST.get('branch')
        user.save()
