from django.shortcuts import render

def listar_estudiantes(request):
    contexto = {
        "estudiantes": [
            {"nombre": "Emanuel", "apellido": "Dautel", "nota": 10},
            {"nombre": "Manuela", "apellido": "Gomez", "nota": 4},
            {"nombre": "Ivan", "apellido": "Tomasevich", "nota": 6},
            {"nombre": "Carlos", "apellido": "Perez", "nota": 1}
        ]
    }
    HttpResponse = render(
        request=request,
        template_name='control_estudios/lista_estudiantes.html',
        context=contexto,
    )
    return HttpResponse

def listar_cursos(request):
    contexto = {
        "cursos": [
            {"nombre": "Fisica", "comision": 1000},
            {"nombre": "Python", "comision": 55350},
            {"nombre": "Redes Sociales", "comision": 2000},
        ]
    }
    HttpResponse = render(
        request=request,
        template_name='control_estudios/lista_cursos.html',
        context=contexto,
    )
    return HttpResponse
