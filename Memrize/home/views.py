from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from home import models

from pathlib import Path


class PoemsIndex(ListView):
    queryset = models.Poem
    context_object_name = "Poems"
    template_name = Path(r"C:\Users\Owner\PycharmProjects\Memrize\Memrize\home\templates\index_page.html")
