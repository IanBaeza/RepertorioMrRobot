from django.shortcuts import render
from .models import Gabinete, Fuente, PlacaMadre, Ram, Procesador, TarjetaVideo, Almacenamiento, Computador

# Create your views here.
def index(request):
	#Número de STOCK en tienda.
	num_gabos=Gabinete.objects.all().count()
	num_fuentes=Fuente.objects.all().count()
	num_placas=PlacaMadre.objects.all().count()
	num_ram=Ram.objects.all().count()
	num_proce=Procesador.objects.all().count()
	num_tvideos=TarjetaVideo.objects.all().count()
	num_almacena=Almacenamiento.objects.all().count()
	

	return render(
		request,
		'index.html',
		context={'num_gabos':num_gabos,'num_fuentes':num_fuentes,'num_placas':num_placas,'num_ram':num_ram,'num_proce':num_proce,'num_tvideos':num_tvideos,'num_almacena':num_almacena},
	)