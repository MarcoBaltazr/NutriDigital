from django.urls import path
from .views import LoginView, DashView, CadastroView, FormView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('cardapio/', DashView.as_view(), name='cardapio'),
    path('cadastro/', CadastroView.as_view(), name='cadastro'),
    path('formulario/', FormView.as_view(), name='formulario'),
]