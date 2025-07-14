from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import PerfilUsuario, Cardapio, Alimento
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages 


class LoginView(TemplateView):
    template_name = 'login.html'

class CadastroView(View):
    def get(self, request):
        return render(request, 'cadastro.html')

    def post(self, request):
        email = request.POST.get('email')
        senha1 = request.POST.get('senha')
        senha2 = request.POST.get('confirmar_senha')

        if not email or not senha1 or not senha2:
            messages.error(request, 'Todos os campos são obrigatórios.')
            return render(request, 'cadastro.html')

        if senha1 != senha2:
            messages.error(request, 'As senhas não coincidem!')
            return render(request, 'cadastro.html')
        
        if User.objects.filter(email=email).exists() or User.objects.filter(username=email).exists():
            messages.error(request, 'Este email já está em uso.')
            return render(request, 'cadastro.html')

        try:
            novo_usuario = User.objects.create_user(username=email, email=email, password=senha1)
            messages.success(request, 'Cadastro realizado com sucesso! Faça o login.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Ocorreu um erro ao criar seu usuário: {e}')
            return render(request, 'cadastro.html')

class FormView(LoginRequiredMixin, View):

    def get(self, request):
        perfil, created = PerfilUsuario.objects.get_or_create(usuario=request.user)
        contexto = {'perfil': perfil}
        return render(request, 'core/formulario.html', contexto)

    def post(self, request):

        perfil, created = PerfilUsuario.objects.get_or_create(usuario=request.user)
        request.user.first_name = request.POST.get('nome')
        perfil.sexo = request.POST.get('sexo')
        perfil.idade = request.POST.get('idade')
        perfil.peso_kg = request.POST.get('peso')
        perfil.altura_cm = request.POST.get('altura')
        perfil.nivel_atividade = request.POST.get('atividade-fisica')
        perfil.objetivo = request.POST.get('objetivo')
        perfil.faixa_renda = request.POST.get('renda')

        request.user.save()
        perfil.save()
        
        # 3. (Futuro) CHAMAR A LÓGICA PARA GERAR O CARDÁPIO
        # gerar_cardapio(request.user)

        # 4. REDIRECIONAR para a página de cardápio (DashView)
        return redirect('cardapio')

class DashView(LoginRequiredMixin, View):

    def get(self, request):
        # Por enquanto, esta view apenas mostra a página HTML.
        # No futuro, vamos buscar o último cardápio do usuário aqui.
        try:
            cardapio = Cardapio.objects.filter(usuario=request.user).latest('data_criacao')
        except Cardapio.DoesNotExist:
            cardapio = None

        contexto = {'cardapio': cardapio}
        return render(request, 'core/cardapio.html', contexto)