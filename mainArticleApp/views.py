from django.shortcuts import render,redirect,HttpResponse
from . import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def index(request):
    allArticles = models.postArticle.objects.all()
    return render(request,'index.html', {'allArticles': allArticles})



def postmyArticle(request):
    if request.method == 'POST':
        heading = request.POST['heading']
        content = request.POST['content']
        dataObj = models.postArticle(article_heading=heading,article_content=content,author=request.user)
        dataObj.save()

    return render(request,'postArticle.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        profession = request.POST['profession']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request,'password is not matching')
            return redirect('register')
        elif len(username) > 10:
            messages.error(request,'username is too long')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.error(request,'username already exists please choose another username!!')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request,'gmail already exists please choose another gmail!!')
            return redirect('register')

        else:
            users = User.objects.create_user(username, email, password)
            users.first_name = first_name
            users.last_name = last_name
            users.profession = profession
            users.save()
            messages.success(request,'You are successfully registered!')
            return redirect('login')
    return render(request,'register.html')


def loggedin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'User logged in')
            return redirect('home')
        else:
            messages.error(request,'There is no user check your username or password')
            return redirect('login')

    return render(request, 'login.html')

def loggedout(request):
    logout(request)
    messages.success(request,'Successfully logged out!')
    return redirect('home')


def showYourArticles(request):
    articles = models.postArticle.objects.filter(author_id=request.user)
    return render(request, 'showYourArticles.html', {'all': articles})


def updateArticle(request,id):
    getid = models.postArticle.objects.get(pk=id)

    if request.method == 'POST':
        getid = models.postArticle.objects.get(pk=id)
        getid.article_heading = request.POST['heading']
        getid.article_content = request.POST['content']
        getid.save()
        messages.success(request, 'You successfully updated your article!')
        return redirect('home')

    return render(request,'update.html',{'paticular_data':getid})



def deleteArticle(request,id):
    if request.method == 'POST':
        getid = models.postArticle.objects.get(pk=id)
        getid.delete()
        messages.success(request, 'You successfully deleted your article!')
        return redirect('home')
    return HttpResponse('404 no page found!')



