from django.urls import path
from . import views

app_name = "MyApp"
urlpatterns = [
    path("", views.index, name = "index"),
    path("book/<int:pk>/", views.bookdetail, name = "book_detail"),
    path('register/author/', views.registerauthor, name='registerauthor'),
    path('register/book/', views.registerbook, name='registerbook'), 
    path('writing/memory/', views.writingmemory, name='writingmemory')
]