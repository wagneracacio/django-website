from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Lembrete, LembreteForm
from django.urls import reverse_lazy

class LembreteListView(ListView):
    model = Lembrete
    template_name = "reminder_list.html"
    context_object_name = 'lembretes'

class LembreteUpdateView(UpdateView):
    model = Lembrete
    form_class = LembreteForm
    template_name = 'reminder_edit.html'
    success_url = reverse_lazy('index')

class LembreteDeleteView(DeleteView):
    model = Lembrete
    template_name = 'reminder_confirm_delete.html'
    success_url = reverse_lazy('index')

class LembreteCreateView(CreateView):
    model = Lembrete
    form_class = LembreteForm
    template_name = 'reminder_edit.html'
    success_url = reverse_lazy('index')
