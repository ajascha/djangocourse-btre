from django.shortcuts import render, redirect

def register(request):
    """
    Test if registration works: put in sth in login box & check terminal output
    print('SUBMITTED REG')
    return redirect('register')
    """
    if request.method == 'POST':
        # Register user
        return
    else:
        return render(request, 'accounts/register.html')



def login(request):
    if request.method == 'POST':
        # Login
        return
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')