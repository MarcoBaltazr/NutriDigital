from django.views.generic import TemplateView

class LoginView(TemplateView):
    template_name = 'login.html'


class DashView(TemplateView):
    template_name = 'cardapio.html'


class CadastroView(TemplateView):
    template_name = 'cadastro.html'


class FormView(TemplateView):
    template_name = 'formulario.html'