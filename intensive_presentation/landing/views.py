from django.views.generic.base import TemplateView

# создаю свою вьюшку
class myOwnView(TemplateView):
    template_name = "presentation.html"

