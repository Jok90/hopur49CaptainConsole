from django.shortcuts import render, get_object_or_404, redirect
from game.forms.game_form import GameCreateForm, GameUpdateForm
from game.models import Game, GameImage


# Create your views here.
def index(request):
    return render(request, 'game/index.html', context={'games': Game.objects.all().order_by('name')})


def get_game_by_id(request, id):
    return render(request, 'game/game_details.html', {
        'game': get_object_or_404(Game, pk=id)
    })


def create_game(request):
    if request.method == 'POST':
        form = GameCreateForm(data=request.POST)
        if form.is_valid():
            game = form.save()
            game_image = GameImage(image=request.POST['image'], game=game)
            game_image.save()
            return redirect('game-index')
    else:
        form = GameCreateForm()
    return render(request, 'game/create_game.html', {
        'form': form
    })


def update_game(request, id):
    instance = get_object_or_404(Game, pk=id)
    if request.method == 'POST':
        form = GameUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('game_details', id=id)
    else:
        form = GameUpdateForm(instance=instance)
    return render(request, 'game/update_game.html', {
        'form': form,
        'id': id
    })


def delete_game(request, id):
    game = get_object_or_404(Game, pk=id)
    game.delete()
    return redirect('game-index')
