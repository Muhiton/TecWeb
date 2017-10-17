from django.http import HttpResponse

def ola(request):
	return HttpResponse("<h1 style='color:Red'>Projeto 1</h1></br><h3>Coisas para colocar.</h3></br><h3>Mais coisas para colocar.</h3>")
	

	