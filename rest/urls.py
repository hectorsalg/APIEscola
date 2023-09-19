from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet, MatriculasViewSet, ListMatriculasAluno, ListAlunosMatriculados
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('curso', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculasViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', ListMatriculasAluno.as_view()),
path('curso/<int:pk>/matriculas/', ListAlunosMatriculados.as_view())
]
