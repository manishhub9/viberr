from django.views import generic
from .models import Album


class IndexView(generic.ListView):
    """docstring for IndexView."""
    template_name = 'music/index.html'
    context_object_name = 'all_albums'
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    """docstring for DetailView."""
    model = Album
    template_name = 'music/detail.html'
