from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin





class TestPage(TemplateView):
    template_name = 'test.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
        else:
            return HttpResponseRedirect(reverse("login"))
        return super().get(request, *args, **kwargs)

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("thanks"))
        else:
            return HttpResponseRedirect(reverse("login"))
        return super().get(request, *args, **kwargs)


class Home(TemplateView):
    template_name = 'index.html'
