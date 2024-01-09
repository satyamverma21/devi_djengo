from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserForm, PatientForm, DoctorForm

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserForm()

    return render(request, 'signup.html', {'form': form})

def login_view(request):
    # Implement login logic here
    pass
