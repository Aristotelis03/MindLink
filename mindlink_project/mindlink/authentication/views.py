from django.shortcuts import render, redirect
# from .models import User
from accounts.models import CustomUser
from django.contrib.auth import login as user_login ,authenticate ,logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm
from django.shortcuts import get_object_or_404
# from django.contrib.auth.forms import AuthenticationForm
# Login view
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            # Log the user in
            # request.session["id"] = user_session.id
                        # Authentication was successful, form.user contains the user object
            
            try:
                user = CustomUser.objects.get(username=form.cleaned_data['username'])
                if user:
                    authentication = authenticate(request, username=user.username, password=form.cleaned_data['password']) 
                    if authentication :
                        request.session["id"] = user.id
                        user_login(request, authentication)
                        return HttpResponseRedirect('/home/')  # Redirect to a success page
                    else:
                            error_message = "Username and Password do not match"
                            return render(request, 'login.html', {'error_message': error_message, 'form': form})
            except CustomUser.DoesNotExist:
                error_message = "User does not exist"
                return render(request, 'login.html', {'error_message': error_message, 'form': form})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)
#         user_session = CustomUser.objects.get(username=username)

#         if user is not None:
#             # Log the user in
#             request.session["id"] = user_session.id
#             user_login(request, user)  # Correct usage
#             return HttpResponseRedirect('/home/')  # Redirect to a success page
#         else:
#             error_message = "Username and Password dose not match"
#             return render(request, 'login.html', {'error_message': error_message})

#     return render(request, 'login.html')
#  View for register
def register_view(request):
    if request.method == 'POST': 
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')  # Redirect to a success page after registration
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('/login')
# Recover view (Uncompleted)
def recover(request):
    return render(request, 'recover.html')

# def register_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         email = request.POST.get('email')
#         # Get the confirmation fron the input
#         confirmation = request.POST['confirmation']

#         # Check if the passwords are the same
#         if password != confirmation:
#             error_message = "Passwords doesn't match"
#             return render(request, "register.html", {'error_message': error_message})
        
#         # Check if the fields are the filled
#         if not username or not password or not email:
#             error_message = "Fill the fields"
#             return render(request,"register.html", {'error_message': error_message})
        

#         # Create a new user
#         user = CustomUser.objects.create_user(username, email, password)
#         # Log the user in
#         return redirect('/login')  # Redirect to a success page after registration

#     return render(request, 'register.html')