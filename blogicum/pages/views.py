from django.views.generic import TemplateView


class AboutView(TemplateView):
    """Статичная страница «О проекте»."""

    template_name = 'pages/about.html'


class RulesView(TemplateView):
    """Статичная страница «Наши правила»."""

    template_name = 'pages/rules.html'
