from django.conf.urls import include, url
#bloquear acceso sabiendose la ruta sin estar logueado
from django.contrib.auth.decorators import login_required
from apps.mascota.views import listadoUsuarios, index, mascota_view, mascota_list, mascota_edit, \
								mascota_delete, MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete


urlpatterns = [
	url(r'^$', index, name = 'index'),
	# url de listar mascota con vista basada en clases
	url(r'^nuevo/$', login_required(MascotaCreate.as_view()), name = 'mascota_crear'),
	url(r'^listar/', login_required(MascotaList.as_view()), name = 'mascota_listar'),
	url(r'^editar/(?P<pk>\d+)/$', login_required(MascotaUpdate.as_view()), name = 'mascota_editar'),
  	url(r'^eliminar/(?P<pk>\d+)/$', login_required(MascotaDelete.as_view()), name = 'mascota_eliminar'),
  	url(r'^listado', listadoUsuarios, name = "listado"),

]