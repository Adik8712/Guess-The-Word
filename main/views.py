from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from main.models import Word, Room, GuessedWord
from main.utils import validator_text, check_word


def index(request):
    if request.user.is_authenticated:
        return redirect('main-page')
    
    return render(request, 'index.html')


def user_registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Имя пользователя уже существует')
                return redirect('sign-up')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Электронная почта уже существует')
                return redirect('sign-up')
        
            else:
                user = User.objects.create_user(
                    username=username, 
                    email=email
                )
                user.set_password(password)
                user.save()
                
                messages.info(request, 'Пользователь успешно создан.')
                
                login(request, user)
                
                return redirect('main-page')
        else:
            messages.info(request, 'Пароли не совпадают')
            return redirect('sign-up')

    return render(request, 'registration.html')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('main-page')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main-page')
            else:
                messages.info(request, 'Неверный логин или пароль')
                return redirect('sign-in')
        else:
            messages.info(request, 'Заполните все поля')
            return redirect('sign-in')
        
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('sign-in')


@login_required(login_url='sign-in')
def main_page(request):
    user_word = Word.objects.filter(creator=request.user)
    user_room = Room.objects.all()

    if request.method == 'POST':
        create_word = request.POST['create_word']
        
        if len(create_word) >= 5:
            if validator_text(create_word):
                word = Word.objects.create(
                    word=create_word,
                    creator=request.user,
                )
                word.save()
                return redirect('main-page')
            else:
                return redirect('main-page')
        else:
            return redirect('main-page')          

    context = {
        "user_words": user_word,
        "user_rooms": user_room
    }

    return render(request, "main.html", context=context)

@login_required(login_url='sign-in')
def room_connection(request, room_id):
    room = Room.objects.get(id=room_id)
    room_word = Word.objects.get(room=room)
    guessed_words = GuessedWord.objects.filter(room=room)

    if request.method == 'POST':
        guessed = request.POST['guessed']

        if validator_text(guessed):
            similar_result: str = check_word(guessed, room_word.word)

            guessed_word = GuessedWord.objects.create(
                word=guessed,
                is_similar=similar_result,
                word_id=room_word,
                creator=request.user,
                room=room,
            )
            guessed_word.save()

            if int(similar_result.split(".")[0]) == 100:
                room.is_closed = True
                room.save()
                return redirect('main-page')

            return redirect('room', room_id=room_id)

    context = {
        "room": room,
        "room_word": room_word,
        "guessed_words": guessed_words,
    }

    return render(request, "room.html", context=context)


