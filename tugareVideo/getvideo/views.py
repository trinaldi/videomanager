# 3rd Party
from google_drive_downloader import GoogleDriveDownloader as gd
from ffmpy import FFmpeg
#Django
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.template import Context, loader

# app
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

def split_link(url):
    url_list = url.split('/')
    url_id = ""
    if (url and len(url_list) > 0):
        url_id = url_list[5] #It might change, be carefull!
        return url_id

def set_thumb(video, timestamp, output):
    video = f'./media/{video}.mp4' #Again, it might change
    output = f'./media/{output}.png'
    thumb = FFmpeg(inputs={video: None},
            outputs={output: ['-ss', timestamp, '-vframes', '1']})
    thumb.run()

def download_link(url, title):
    file_id = split_link(url)
    gd.download_file_from_google_drive(
        file_id = file_id,
        dest_path = "./media/{}.mp4".format(title) # We'll treat it leater, ok?
    )

def create(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            download_link(request.POST.get('video_url'),
                        request.POST.get('video_title'))
            set_thumb(request.POST.get('video_title'),
                    request.POST.get('video_thumb'),
                    request.POST.get('video_title'))
            form.save()
            return redirect('index')
    form = VideoForm()

    return render(request, 'videos/create.html', {'form': form})

def edit(request, pk, template_name='videos/edit.html'):
    context = {}
    video = get_object_or_404(Video, id=pk)
    form = VideoForm(request.POST or None, instance=video)
    if form.is_valid():
        download_link(request.POST.get('video_url'),
                request.POST.get('video_title'))
        form.save()
        return redirect('index')
    context["form"] = form
    return render(request, template_name, {'form':form})

def delete(request, pk, template_name='videos/delete.html'):
    context = {}
    video = get_object_or_404(Video, pk=pk)
    if request.method=='POST':
        video.delete()
        return redirect('index')
    context["video"] = video
    return render(request, template_name, {'video':video})
