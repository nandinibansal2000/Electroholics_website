from django.views.generic import TemplateView , ListView
from .models import Session

class TableView(ListView):
    template_name = 'session.html'

    def get_queryset(self):
        return Session.objects.all()
