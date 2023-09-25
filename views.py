from django.shortcuts import render, redirect, get_object_or_404
from .models import Idea
from .forms import IdeaForm

def idea_list(request):
    ideas = Idea.objects.all()
    return render(request, 'ideas/idea_list.html', {'ideas': ideas})

def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    return render(request, 'ideas/idea_detail.html', {'idea': idea})

def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()
            return redirect('idea_detail', pk=idea.pk)
    else:
        form = IdeaForm()
    return render(request, 'ideas/idea_form.html', {'form': form})

def idea_edit(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('idea_detail', pk=idea.pk)
    else:
        form = IdeaForm(instance=idea)
    return render(request, 'ideas/idea_form.html', {'form': form})

def idea_delete(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == 'POST':
        idea.delete()
        return redirect('idea_list')
    return render(request, 'ideas/idea_confirm_delete.html', {'idea': idea})

def home(request):
    # Aquí puedes agregar lógica para mostrar los posts en la página de inicio
    return render(request, 'ideas/idea_list.html')  # Renderiza la plantilla ideas/idea_list.html


def about_view(request):
    return render(request, 'about.html')  # Asegúrate de que tengas una plantilla llamada 'about.html'

