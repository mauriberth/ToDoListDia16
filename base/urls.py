from django.urls import path
from .views import PendingList, DetailTask, CreateTask, UpdateTask, DeleteTask, Log, Register
from django.contrib.auth.views import LogoutView

urlpatterns = [path('', PendingList.as_view(), name='tasks'),
               path('login/', Log.as_view(), name='login'),
               path('register/', Register.as_view(),name='register'),
               path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
               path('task/<int:pk>', DetailTask.as_view(), name='task'),
               path('create-task/', CreateTask.as_view(), name='create-task'),
               path('edit-task/<int:pk>', UpdateTask.as_view(), name='update-task'),
               path('delete-task/<int:pk>', DeleteTask.as_view(), name='delete-task')],
