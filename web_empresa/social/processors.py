
from .models import Link

def contexto_dict(request):
    contexto = {}
    links = Link.objects.all()
    for link in links:
        contexto[link.key] = link.url
        #print("contexto {0}".format(link.key))
        #print("url {0}".format(link.url))
    return contexto