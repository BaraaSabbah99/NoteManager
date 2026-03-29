
from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
    path('addNote/',views.addNote,name='addnote'),
    path('',views.mynotes,name='mynotes'),
    path('deleteNote/<int:noteid>/',views.deletenote,name='deletenote')
  
]
