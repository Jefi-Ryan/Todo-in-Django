"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todolist import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('create/',views.CreateTodo.as_view(),name='create'),
    path('list/',views.ListTodo.as_view(),name='List'),
    path('list/delete/<int:id>',views.DeleteTodo.as_view(),name='Deletelist'),
    path('list/search/',views.SearchTodoList.as_view(),name='Searchlist'),
    path('list/search/delete/<int:id>',views.DeleteTodoSearch.as_view(),name='Deletesearchlist'),
    path('list/search/update/<int:id>',views.UpdateTodoSearch.as_view(),name='Updatesearchlist'),
    path('list/update/<int:id>',views.UpdateTodo.as_view(),name='Updatelist'),
    path('list/detail/update/<int:id>',views.UpdateTodo.as_view(),name='Updatedetail'),
    path('list/detail/delete/<int:id>',views.DeleteTodo.as_view(),name='Deletedetail'),
    path('list/detail/',views.DetailTodo.as_view(),name='Detail'),
    path('list/detail/search/',views.SearchTodoDetail.as_view(),name='Searchdetail'),
    path('list/detail/search/update/<int:id>',views.UpdateTodoSearch.as_view(),name='Updatesearchdetail'),
    path('list/detail/search/delete/<int:id>',views.DeleteTodoSearch.as_view(),name='Deletesearchdetail'),
    
    
   
    
]
