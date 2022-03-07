from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm

# Create your views here.
def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    form = AlbumForm()
    return render(request, "album_detail.html", {"album": album, "form": form})

def list_albums(request):
    albums = Album.objects.all()
    return render(request, "list_albums.html", {"albums": albums})

def add_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "add_album.html", {"form": form})

def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "edit_album.html", {"form": form, "album": album})

def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')

    return render(request, "delete_album.html", {"album": album})