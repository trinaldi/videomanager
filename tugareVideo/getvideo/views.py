from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Video
from .forms import VideoForm

class IndexView(ListView):
    template_name = 'videos/index.html'
    context_object_name = 'video_list'

    def get_queryset(self):
        return Video.objects.all()

class VideoDetailView(DetailView):
    template_name = 'videos/detail.html'
    model = Video

    def get_field_values(self):
        return [field.value_to_string(self) for field in Video._meta.fields]

def create(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = VideoForm()

    return render(request, 'videos/create.html', {'form': form})

def edit(request, pk, template_name='videos/edit.html'):
    video = get_object_or_404(Video, pk=pk)
    form = VideoForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

def delete(request, pk, template_name='videos/confirm_delete.html'):
    video = get_object_or_404(Video, pk=pk)
    if request.method=='POST':
        video.delete()
        return redirect('index')
    return render(request, template_name, {'object':video})
