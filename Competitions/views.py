from django.views.generic import TemplateView , ListView
from .models import Competition

class TableView(ListView):
    template_name = 'competition.html'

    def get_queryset(self):
        return Competition.objects.all()