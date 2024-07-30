from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('todo/',views.todo,name='todo'),
    path('add_todo/',views.add_todo,name='add_todo'),
    path('delete_todo/<int:id>',views.delete_todo,name='delete_todo'),
    path('update_todo/<int:id>',views.update_todo,name='update_todo'),
    path('mark_completed/<int:id>',views.mark_completed,name='mark_completed'),
    path('upload_profile/',views.upload_profile,name='upload_profile')
]

