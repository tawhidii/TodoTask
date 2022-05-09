from django.urls import path

from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.TodoHomeView.as_view(), name='home'),
    path('create/', views.TodoCreateView.as_view(), name='create-todo'),
    path('update/<int:pk>/', views.TodoUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.TodoDeleteView.as_view(), name='delete'),
    path('category/<int:pk>/',views.CategoryFilterView.as_view(),name='filter-category')
]
