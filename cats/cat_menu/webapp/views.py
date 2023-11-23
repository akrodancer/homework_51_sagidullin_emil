from django.shortcuts import render
from webapp.cat import Cat
from django.http import HttpResponseRedirect

# Create your views here.
def create_cat_menu(request):
    if request.method == 'GET':
        return render(request, 'create_menu.html')
    elif request.method == 'POST':
        global cat
        cat = Cat(name=request.GET.get('name'))
        context = {'name': cat.name,
                   'food': cat.food,
                   'mood': cat.mood,
                   'age': cat.age,
                   'img': cat.img}
        return render(request, 'main_menu.html', context)

def action(request):
    action = request.GET.get('action')
    match action:
        case 'feed': cat.feed()
        case 'play': cat.play()
        case 'change_state': cat.change_state()
    return HttpResponseRedirect('/')



