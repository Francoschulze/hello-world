from django.http import HttpResponse


# Importamos o o HttpResponse para que seja retornado um objeto
# De resposta com a string definida na função 'Hello, World'
def home_page_view(request):
    return HttpResponse('Hello, World')
