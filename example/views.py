from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import FirstForm, SecondForm


class RequestFormMixin:
    """Mixin to inject the request in the form."""

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs


class FirstView(RequestFormMixin, FormView):
    """Implémente la première étape: le téléchargement du fichier."""

    template_name = 'example/first.html'
    form_class = FirstForm
    success_url = reverse_lazy('second')


class SecondView(RequestFormMixin, FormView):
    """Implémente la seconde étape: le choix multiple dynamique."""

    template_name = 'example/second.html'
    form_class = SecondForm
    success_url = reverse_lazy('third')


class ThirdView(TemplateView):
    """Implémente la vue qui affiche le contenu du fichier."""

    template_name = 'example/third.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['uploaded'] = self.request.session['uploaded']
        context['selection'] = self.request.session['selection']
        return context
