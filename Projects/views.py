from django.views.generic import TemplateView , ListView
from .models import Project

class TableView(ListView):
    template_name = 'project.html'

    def get_queryset(self):
        return Project.objects.all()