from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from game.forms.game_form import GameCreateForm, GameUpdateForm
from game.models import Game, GameImage
import logging

# Create your views here.
def index(request):
    # logging.error('----------+> body: %s query: %s' % (request.body, request.query ))
    orderBy = request.GET.get('orderby_dropdown', 'name').lower()
    logging.error('orderBy %s' % orderBy)

    games = Game.objects.all()

    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        games = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.gameimage_set.first().image
        } for x in Game.objects.filter(name__icontains=search_filter).order_by(orderBy) ]
        return JsonResponse({'data': games})
    if 'category' in request.GET:
        category = request.GET['category']
        # games = [{
        #     'id': x.id,
        #     'name': x.name,
        #     'description': x.description,
        #     'firstImage': x.gameimage_set.first().image
        # } for x in Game.objects.filter(developer__exact=category).order_by(orderBy)]
        # return JsonResponse({'data': games})
        if category != 'all':
            games = games.filter(developer__name__iexact=category)

    return render(request, 'game/index.html', context={'games': games.order_by(orderBy)})



def get_game_by_id(request, id):
    return render(request, 'game/game_details.html', {
        'game': get_object_or_404(Game, pk=id)
    })

def create_game(request):
    if request.user.is_staff or request.user.is_superuser:
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
    else:
        return HttpResponse(status=403)

def update_game(request, id):
    if request.user.is_staff or request.user.is_superuser:
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
    else:
        return HttpResponse(status=403)


def delete_game(request, id):
    if request.user.is_staff or request.user.is_superuser:
        game = get_object_or_404(Game, pk=id)
        game.delete()
        return redirect('game-index')
    else:
        return HttpResponse(status=403)