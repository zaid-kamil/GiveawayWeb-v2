from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from .forms import UserLoginForm, UserRegistration
from products.models import Product, Giveaway


# Create your views here.
def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("/")
    context = {"forms": form, 'tab_active': 'login','title':'Login to Website'}
    return render(request, "login.html", context)


def register_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Register"
    form = UserRegistration(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("/")
    context = {
        "form": form,
        "title": title
    }
    return render(request, "register.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")


def show_dash(request):
    # Product.objects.filter(creator=request.user)
    # Giveaway.objects.filter(creator=request.user)

    context = {}
    return render(request, 'profile_dashboard.html', context)