import django_filters
from . models import Notes
class NoteFilter(django_filters.FilterSet):
    
    class Meta:
        model = Notes
        fields = {
            'sub' : ['exact'],
            'mod' : ['exact'],
            'typeN' : ['exact'],
        }
