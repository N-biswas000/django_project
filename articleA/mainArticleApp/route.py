from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('postmyarticle/',views.postmyArticle, name='postmyArticle'),
    path('login/',views.loggedin, name = 'login'),
    path('register/',views.register, name = 'register'),
    path('logout/',views.loggedout, name = 'logout'),
    path('showYourArticles/',views.showYourArticles, name = 'showYourArticles'),
    path('update/<int:id>',views.updateArticle, name = 'updateArticle'),
    path('delete/<int:id>',views.deleteArticle, name = 'deleteArticle')
]