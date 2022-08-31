from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppCoder.models import  Familia

def familia(request):
    
    familia1 = Familia(
        nombre="Bob",
        apellido = "OviedoPadula",
        edad=15,
        fecha_ingreso=datetime.now()
    )
   
    familia2 = Familia(
        nombre="Mica",
        apellido = "Oviedo",
        edad=25,
        fecha_ingreso=datetime.now()
    )

    familia3= Familia(
        nombre="Luca",
        apellido = "Padula",
        edad=27,
        fecha_ingreso=datetime.now()

    )

    familia1.save()
    familia2.save()
    familia3.save()

    familia_list=[familia1, familia2, familia3]
    diccionario={"lista":familia_list}

    plantilla=loader.get_template("familia.html")
    doc=plantilla.render(diccionario)


    return HttpResponse(doc)

