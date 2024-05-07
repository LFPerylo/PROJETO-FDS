
from django.contrib import admin
from django.urls import path, include
from webapp import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.login, name="login"),
    path('dicas/', views.dicas, name="dicas"),
    path('home_aluno/', views.home_aluno, name="home_aluno"),
    path('home_adm/', views.home_adm, name="home_adm"),
    path('treinospredefinidos/', views.treinospredefinidos, name="treinospredefinidos"),
    path('duvidas/', views.duvidas, name="duvidas"),
    path('marcar_consulta/',views.marcar_consulta, name="marcar_consulta"),
    path('progresso/',views.progresso, name="progresso"),
    path('feedback/',views.feedback, name="feedback"),
    path('registrar_progresso/', views.registrar_progresso, name='registrar_progresso'),
    path('processar_formulario/', views.processar_formulario, name="processar_formulario"),
    path('registrar_progresso/', views.registrar_progresso, name="registrar_progresso"),
    path('enviar_feedback/', views.enviar_feedback, name="enviar_feedback"),
    path('enviar_duvida/', views.enviar_duvida, name='enviar_duvida'),
    path('mostrar_progressos/', views.mostrar_progressos, name='mostrar_progressos'),
    path('admin/', admin.site.urls)
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
