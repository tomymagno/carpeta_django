from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


def saludar(request):
    saludo = "Hola querido usuario"
    pagina_html = HttpResponse(saludo)
    return pagina_html

def saludar_con_html(request):
    http_response = render(
        request=request,
        template_name="base.html",
        context={},
    )
    return http_response