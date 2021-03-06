from django.contrib import messages, auth

from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse

from django.shortcuts import render, redirect

from django.template.context_processors import csrf

from accounts.forms import UserRegistrationForm, UserLoginForm

# Create your views here.

def register(request, register_form=UserRegistrationForm):

    if request.method == 'POST':

        form = register_form(request.POST)

        if form.is_valid():

            form.save()

            user = auth.authenticate(email=request.POST.get('email'), password=request.POST.get('password1'))

            if user:

                messages.success(request, "You have sucessfully registered")

                return redirect(reverse('login'))

            else:

                messages.error(request, "unable to log you in at this time!")

    else:

        form = register_form()

    args = {'form': form }

    args.update(csrf(request))

    return render(request, 'register.html', args)

def login(request, success_url=None):

    if request.method == 'POST':

        form = UserLoginForm(request.POST)

        if form.is_valid():

            user = auth.authenticate(email=request.POST.get('email'), password=request.POST.get('password'))

            if user is not None:

                auth.login(request, user)

                messages.error(request, "You have sucessfully logged in")

                return redirect(reverse('profile'))

            else:

                form.add_error(None, "Your email or password was not recognised")

    else:

        form = UserLoginForm()

    args = {'form':form}

    args.update(csrf(request))

    return render(request, 'login.html', args)


@login_required(login_url='/accounts/login/')

def profile(request):

    return render(request, "profile.html")

def logout(request):

    auth.logout(request)

    messages.success(request, "You have successfully logged out")

    return render(request, 'index.html')

