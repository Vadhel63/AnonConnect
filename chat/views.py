from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
import secrets
import string

def home(request):
    rooms = Room.objects.all()
    return render(request, 'home.html',{'rooms': rooms})

def room(request, room):
    characters = string.ascii_letters + string.digits
    username = ''.join(secrets.choice(characters) for i in range(8))
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/')
    else:
        new_room = Room.objects.create(name=room)
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