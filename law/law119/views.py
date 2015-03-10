from django.shortcuts import render
from .import models
from django.views import generic

# Create your views here.

class home(generic.ListView):
    queryset = models.Entry.object.published()
    template_name = "law119/index.html"
    paginate_by = 2

class Detail(generic.DetailView):
    # model = models.Entry
    template_name = "law119/post.html"
