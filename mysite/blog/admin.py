from django.contrib import admin
from .models import Post
from .models import Aluno
from .models import TurmaAluno
from .models import Turma

admin.site.register(Post)
admin.site.register(Aluno)
admin.site.register(Turma)
admin.site.register(TurmaAluno)

# Register your models here.
# Estou modificando aqui para fazer um teste
