from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Joke
from .forms import JokeForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return HttpResponse("Hi, how are you doing?")

# 查看所有笑話
def joke_list(request):
    jokes = Joke.objects.all()
    return render(request, 'joke_list.html', {'jokes': jokes})

# 添加新的笑話
@login_required
def add_joke(request):
    if request.method == 'POST':
        form = JokeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('joke_list')
    else:
        form = JokeForm()
    return render(request, 'add_joke.html', {'form': form})

# 刪除笑話
@login_required
def delete_joke(request, id):
    joke = get_object_or_404(Joke, id=id)
    if request.method == 'POST':
        joke.delete()
        return redirect('joke_list')
    return render(request, 'delete_joke.html', {'joke': joke})