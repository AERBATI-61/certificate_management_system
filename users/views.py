from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

def register(request):

    if request.method == "POST":
        username = request.POST["username"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {
                    "error": "bu ad kullaniliyor.",
                    "username": username,
                    "email": email,
                })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, 'register.html', {
                        "error": "bu email kullaniliyor.",
                        "username": username,
                        "email": email,
                    })
                else:
                    user = User.objects.create_user(username=username, last_name=lastname, email=email, password=password)
                    user.save()
                    return redirect('login')
        else:
            return render(request, 'register.html', {
                "error": "Parola eslesmiyor.",
                "username": username,
                "emial": email,
            })

    return render(request, "register.html")


def loginUser(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "login.html", {
                "error": "username veya parola yanlis"
            })
    else:
        return render(request, "login.html")


def logoutUser(request):
    logout(request)
    return redirect("index")
    pass

