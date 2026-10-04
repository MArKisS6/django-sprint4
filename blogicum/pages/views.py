from django.shortcuts import render
from django.views.generic import TemplateView


class AboutView(TemplateView):
    """Статичная страница «О проекте»."""

    template_name = 'pages/about.html'


class RulesView(TemplateView):
    """Статичная страница «Наши правила»."""

    template_name = 'pages/rules.html'


def page_not_found(request, exception):
    """Кастомная страница 404."""
    return render(request, 'pages/404.html', status=404)


def csrf_failure(request, reason=''):
    """Кастомная страница 403 (CSRF)."""
    return render(request, 'pages/403csrf.html', status=403)


def custom_500(request):
    """Кастомная страница 500."""
    return render(request, 'pages/500.html', status=500)
