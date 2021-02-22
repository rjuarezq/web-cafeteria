from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage

from .forms import ContactForm
# Create your views here.


def contact(request):
    # Creamos plantilla vacia
    contact_form = ContactForm()

    # Verificación si se envio algun dato al servidor
    if request.method == 'POST':

        # Relllenamos la plantilla automaticamente con la información
        contact_form = ContactForm(data=request.POST)

        # Verificamos si todos los campos estan correctos
        if contact_form.is_valid():

            # recuperamos los campos
            name = request.POST.get('nombre', '')
            email = request.POST.get('email', '')
            content = request.POST.get('contenido', '')

            # Si toda las instrucciones estan OK redireciconamos
            # REPLY_TO(pasaremos el email donde va a responder la persona que recibira este correo)
            subject = "RESTAURANTE: Nuevo mensaje de contacto"
            body = "De: {} <{}>\n\nEscribio:\n\n{}".format(name, email, content)
            from_email = "no-contestar@inbox.mailtrap.io"
            to = ['developerricardo20@gmail.com',
                    'zoscogames@gmail.com'] 
            
            
            # correo = EmailMessage(
            #     "RESTAURANTE: Nuevo mensaje de contacto",  # ASUNTO
            #     "De: {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
            #     "no-contestar@inbox.mailtrap.io",
            #     ['developerricardo20@gmail.com',
            #         'zoscogames@gmail.com'],  # EMAIL_DESTINO
            #     reply_to=[email])
            
            correo = EmailMessage(subject,body, from_email,to, reply_to=[email])
            
            try:
                correo.send()
                return redirect(reverse('contact_form') + "?ENVIADO")

            except:
                return redirect(reverse('contact_form') + "?FALLIDO")

    return render(request, 'contact/contact.html', {'form': contact_form})
