from django.urls import path
from . import views

app_name = "MyApp"
urlpatterns = [
    path("", views.index, name = "index"),
    path("book/<int:pk>/", views.bookdetail, name = "book_detail"),
    path('register/author/', views.registerauthor, name='registerauthor'),
    path('register/book/', views.registerbook, name='registerbook'), 
    path('writing/thismemory/<int:pk>/', views.writingthisbookmemory, name='writingthismemory'),
    path('writing/memory/<int:pk>/', views.writingmemory, name='writingmemory'),
    path('update/memory/<int:pk>/', views.updatememory, name='updatememory'),
    path('delete/memory/<int:pk>/', views.deletememory, name='deletememory'),
    path('delete/book/<int:pk>/', views.deletebook, name='deletebook')
]