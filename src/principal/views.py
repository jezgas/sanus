from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse



from django.views.generic import ListView, CreateView
from django.core.urlresolvers import reverse_lazy
from models import Precios
from principal.forms import PreciosForm, Registroform
from django.core.mail import send_mail
# Create your views here.

def inicio(request):
	
	return render(request, "inicio.html", {})




def contacto(request):
	
	return render(request, "contacto.html", {})



def servicios(request):
	
	return render(request, "servicios.html", {})



class listarprecios(ListView):
	model = Precios
	template_name = 'precios.html'



def contacto(request):
	form = Registroform(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_mensaje = form.cleaned_data.get("mensaje")
		form_nombre = form.cleaned_data.get("nombre")
		asunto = 'Form de Contacto'
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from, "lavanderiasanus@gmail.com"]
		email_mensaje = "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email)
		send_mail(asunto,
		 	email_mensaje,
		 	email_from,
		 	email_to,
		 	fail_silently=False
		 	)
		#print nombre, email, mensaje
		return HttpResponseRedirect('gracias')
	context = {
		"form": form,
	}
	return render(request, "contacto.html", context)

# def precios(request):
# 	form = PreciosForm()
# 	context = {
# 		"form": form,
# 	}
# 	return render(request, "precios.html", context)
