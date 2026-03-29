from django.shortcuts import render , redirect
from .models import Note
from Users.models import User

# Create your views here.


def addNote(request):
    try:
        role = request.session['role']
    except:
        role = None
    if role == None:
        return redirect('users:login')
    elif role == 'user':
        if request.method == 'POST':
         title = request.POST.get('title')
         content = request.POST.get('content')
         user = User.objects.get(id=request.session['id'])
         note = Note(title=title,content=content,TheAuthor=user)
         note.save()
         return redirect('notes:mynotes')
        else:
            return render(request,'addNote.html')
    else :
        return redirect('users:login')




def mynotes(request):
    try:
        role = request.session['role']
    except:
        role = None
    if role == None:
        return redirect('users:login')
    elif role =='user':
     user = User.objects.get(id=request.session['id'])
     notes=Note.objects.filter(TheAuthor=user)
     return render(request,'mynotes.html',{"notes":notes})
    else:
        return redirect('users:login')




def deletenote(request,noteid):
    try:
        role = request.session['role']
    except:
        role = None
    if role == None:
        return redirect('users:login')
    elif role == 'user':

      note = Note.objects.get(id=noteid)
      note.delete()
      return redirect('notes:mynotes')
    else :
        return redirect('users:login')

