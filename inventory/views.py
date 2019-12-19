from django.views.generic import TemplateView , ListView
from .models import Entry

class TableView(ListView):
    template_name = 'table.html'

    def get_queryset(self):
        return Entry.objects.all()
