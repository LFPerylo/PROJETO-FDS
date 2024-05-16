from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from .models import Dados, Dica
from .models import Feedback
from .forms import FeedbackForm 
from .forms import ProgressoForm
from .models import Duvida
from .models import Consulta,TreinoPredefinido,Progresso
from .forms import CadastroForm, LoginForm, DicaForm,ConsultaForm,TreinoPredefinidoForm
from .models import Imagem
from datetime import datetime


def login(request):
    imagens = Imagem.objects.all()
    return render(request, 'front/login.html', {'imagens': imagens})

def cadastro(request):
    imagens = Imagem.objects.all()
    return render(request, 'front/cadastro.html', {'imagens': imagens})

def dicas(request):

    return render(request, 'dicas.html')

def info(request):

    return render(request, 'info.html')

def dicas_adm(request):

    return render(request, 'dicas_adm.html')

def home_aluno(request, nome_usuario=None):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        if tipo == 'administrador':
            return redirect('/home_adm/')
        elif tipo == 'aluno':
            return redirect('/home_aluno/')
        else:
            return HttpResponse("Usuário ou senha inválidos", status=401)
    return render(request, 'home_aluno.html', {'nome_usuario': nome_usuario})

def home_adm(request):
    usuarios = Dados.objects.all()  
    return render(request, 'home_adm.html', {'usuarios': usuarios})

def duvidas(request):

    return render(request,'duvidas.html')

def treinospredefinidos(request):

    return render(request,'treinospredefinidos.html')

def treinospredefinidos_adm(request):

    return render(request, 'treinospredefinidos_adm.html')

def marcar_consulta(request):

    return render(request, 'marcar_consulta.html')

def marcar_consulta_adm(request):

    return render(request,'marcar_consulta_adm.html')

def progresso(request):

    return render(request,'progresso.html')

def progresso_adm(request):

    return render(request, 'progresso_adm.html')

def feedback(request):

    return render(request,'feedback.html')

def feedback_aluno(request):

    return render(request, 'feedback_aluno.html')

def registrar_progresso(request):
    mensagem_erro = None
    mensagem_sucesso = None

    if request.method == 'POST':
        form = ProgressoForm(request.POST)
        if form.is_valid():
            nome_aluno = form.cleaned_data['nome_aluno']
            tipo_progresso = form.cleaned_data['tipo_progresso']
            observacao = form.cleaned_data['observacao']
            data = form.cleaned_data['data']

            
            if Dados.objects.filter(nome=nome_aluno, tipo='usuario').exists():
                aluno = Dados.objects.get(nome=nome_aluno, tipo='usuario')
                
                progresso = Progresso.objects.create(nome_aluno=aluno, tipo_progresso=tipo_progresso, observacao=observacao, data=data)
                mensagem_sucesso = "Progresso registrado com sucesso!"
            else:
                mensagem_erro = "Usuário não cadastrado ou não é aluno."
        else:
            mensagem_erro = "Formulário inválido. Por favor, verifique os dados informados."
    else:
        form = ProgressoForm()

    return render(request, 'progresso.html', {'form': form, 'mensagem_erro': mensagem_erro,'mensagem_sucesso':mensagem_sucesso})

def enviar_duvida(request):
    if request.method == 'POST':
        duvida_escrita = request.POST.get('duvidaescrita')
        nome_treinador = request.POST.get('treinador')
        
    
        duvida = Duvida(duvida_escrita=duvida_escrita, nome_treinador=nome_treinador)
        duvida.save()
        
    
        return redirect('/duvidas/')
    else:
        return redirect('/duvidas/')
    

def enviar_feedback(request):
    mensagem_erro = ""
    mensagem_sucesso = ""
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            nome_aluno = form.cleaned_data['nome_aluno']
            feedback_texto = form.cleaned_data['feedback']

            
            if Dados.objects.filter(nome=nome_aluno, tipo='usuario').exists():
                aluno = Dados.objects.get(nome=nome_aluno)
                feedback = Feedback.objects.create(feedback=feedback_texto, aluno=aluno)
                mensagem_sucesso = "Feedback registrado com sucesso!"
            else:
                form.add_error('nome_aluno', 'Aluno não encontrado ou não é um usuário.')
                mensagem_erro = "Aluno não encontrado ou não é um usuário."
                print(mensagem_erro)

    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form, 'mensagem_erro': mensagem_erro, 'mensagem_sucesso': mensagem_sucesso})

def agendar_consulta(request):
    mensagem_sucesso=""
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid(): 
            form.save() 
            mensagem_sucesso = "consulta marcada com sucesso"  
    else:
        form = ConsultaForm() 

    return render(request, 'marcar_consulta.html', {'form': form,'mensagem_sucesso': mensagem_sucesso})

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CadastroForm()
    return render(request, 'cadastro.html', {'form': form})


def fazer_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            senha = form.cleaned_data['senha']
            tipo = form.cleaned_data['tipo']
            
            usuario = Dados.objects.filter(nome=nome, senha=senha, tipo=tipo).first()
            if usuario:
                if tipo == 'usuario':
                    
                    return redirect('/home_aluno/')  
                elif tipo == 'administrador':
                    
                    return redirect('/home_adm/')
            
            erro = 'Usuário não cadastrado ou credenciais incorretas.'
    else:
        form = LoginForm()
        erro = None
    return render(request, 'front/login.html', {'form': form, 'erro': erro})

def adicionar_dica(request):
    mensagem_sucesso=""
    if request.method == 'POST':
        form = DicaForm(request.POST)
        if form.is_valid():
            form.save()
            mensagem_sucesso= "Dica adicionada com sucesso"
    else:
        form = DicaForm()
    return render(request, 'dicasadm.html', {'form': form, 'mensagem_sucesso':mensagem_sucesso})

def exibir_dica(request):
    tipo_selecionado = request.GET.get('tipo')
    dicas = Dica.objects.filter(tipo=tipo_selecionado) if tipo_selecionado else None
    return render(request, 'dicas.html', {'dicas': dicas})

def criar_treino_predefinido(request):
    mensagem_sucesso=""
    if request.method == 'POST':
        form = TreinoPredefinidoForm(request.POST)
        if form.is_valid():
            form.save()
            mensagem_sucesso= "Treino Criado com sucesso"
            
            
    else:
        form = TreinoPredefinidoForm()

    return render(request, 'treinospredefinidos_adm.html', {'form': form, 'mensagem_sucesso':mensagem_sucesso})


def exibir_treino_predefinido(request):
    tipo_treino = request.GET.get('tipo_treino')
    treinos = None
    
    if tipo_treino:
        treinos = TreinoPredefinido.objects.filter(tipo_treino=tipo_treino)
    
    return render(request, 'treinospredefinidos.html', {'treinos': treinos})

def exibir_feedback(request):
    if request.method == 'GET':
        nome_aluno = request.GET.get('nome_aluno')

        if nome_aluno:
            try:
                aluno = Dados.objects.get(nome=nome_aluno, tipo='usuario')
                feedbacks = Feedback.objects.filter(aluno=aluno)
                return render(request, 'feedback_aluno.html', {'feedbacks': feedbacks, 'nome_aluno': nome_aluno})
            except Dados.DoesNotExist:
                mensagem_erro = "Aluno não encontrado no banco de dados."
            except Feedback.DoesNotExist:
                mensagem_erro = "Não há feedback para este aluno."
            except Exception as e:
                mensagem_erro = str(e)

            return render(request, 'feedback_aluno.html', {'mensagem_erro': mensagem_erro})

        else:
            return render(request, 'feedback_aluno.html')

    return render(request, 'feedback_aluno.html')

def exibir_consultas(request):
    if request.method == 'GET':
        data_selecionada = request.GET.get('data')
        if data_selecionada:
            try:
                
                data_selecionada = datetime.strptime(data_selecionada, '%Y-%m-%d').date()
                consultas = Consulta.objects.filter(data=data_selecionada)
                return render(request, 'marcar_consulta_adm.html', {'consultas': consultas, 'data_selecionada': data_selecionada})
            except ValueError:
                mensagem_erro = "Formato de data inválido."
                return render(request, 'marcar_consulta_adm.html', {'mensagem_erro': mensagem_erro})
        else:
            mensagem_erro = "Nenhuma data selecionada."
            return render(request, 'marcar_consulta_adm.html', {'mensagem_erro': mensagem_erro})
    else:
    
        pass

def exibir_progresso(request):
    mensagem_erro = None
    progressos = None

    if request.method == 'POST':
        nome_aluno = request.POST.get('nome_aluno')

        # Verificar se o aluno existe e é do tipo "usuário"
        if Dados.objects.filter(nome=nome_aluno, tipo='usuario').exists():
            aluno = Dados.objects.get(nome=nome_aluno, tipo='usuario')
            # Verificar se o aluno possui progresso registrado
            progressos = Progresso.objects.filter(nome_aluno=aluno)
            if not progressos:
                mensagem_erro = "Este usuário não possui nenhum progresso registrado."
        else:
            mensagem_erro = "Usuário não cadastrado ou não é usuário."

    return render(request, 'progresso_adm.html', {'mensagem_erro': mensagem_erro, 'progressos': progressos})

def exibir_informacoes(request):
    if request.method == 'POST':
        nome_desejado = request.POST.get('nome_aluno', None)

        if nome_desejado:
            # Filtrar os feedbacks pelo nome desejado
            feedbacks = Feedback.objects.filter(aluno__nome=nome_desejado)

            # Filtrar o progresso pelo nome desejado
            progressos = Progresso.objects.filter(nome_aluno__nome=nome_desejado)

            if not feedbacks.exists() and not progressos.exists():
                mensagem = f"O aluno '{nome_desejado}' não possui feedbacks nem progresso registrados."
            else:
                mensagem = None

            context = {
                'feedbacks': feedbacks,
                'progressos': progressos,
                'mensagem': mensagem
            }
            return render(request, 'exibir_informacoes.html', context)
        else:
            mensagem = "Por favor, insira um nome de aluno válido."
    else:
        mensagem = None

    return render(request, 'form_busca_aluno.html', {'mensagem': mensagem})
