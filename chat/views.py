from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
import secrets
import string


def home(request):
    rooms = Room.objects.all()
    return render(request, 'home.html',{'rooms': rooms})

def room(request, room):
    characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','-','_']
    username = ''.join(secrets.choice(characters) for i in range(8))
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })
def jointeam(request):
    code=request.POST['join']
    if Room.objects.filter(name=code).exists():
      return redirect('/'+code+'/')
    else:
        return HttpResponse("NO TEAM AVAILABLE")
def checkview(request):
    room = request.POST['room_name']
    abc=request.POST['prefer']
    
    if Room.objects.filter(name=room ,type=abc).exists():
        return redirect('/'+room+'/')
    elif Room.objects.filter(name=room):
        return render(request,'error.html')
    else:
        new_room = Room.objects.create(name=room,type=abc)
        new_room.save()
        return redirect('/'+room+'/')

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})


