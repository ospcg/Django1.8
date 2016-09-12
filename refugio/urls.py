from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^mascota/', include('apps.mascota.urls', namespace = 'mascota')),
    url(r'^adopcion/', include('apps.adopcion.urls', namespace = 'adopcion')),
    url(r'^solicitud/', include('apps.adopcion.urls', namespace = 'solicitud')),
    url(r'^usuario/', include('apps.usuario.urls', namespace = 'usuario')),
    url(r'^accounts/login/',login, {'template_name':'index.html'}, name= 'login'),
    url(r'^logout/',logout_then_login, name= 'logout'),
    url(r'^reset/password_reset', password_reset, 
        {'template_name':'registration/password_reset_form.html',
        'email_template_name': 'registration/password_reset_email.html'}, 
        name='password_reset'), 
    url(r'^reset/password_reset_done', password_reset_done, 
        {'template_name': 'registration/password_reset_done.html'}, 
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, 
        {'template_name': 'registration/password_reset_confirm.html'},
        name='password_reset_confirm'
        ),
    url(r'^reset/done', password_reset_complete, {'template_name': 'registration/password_reset_complete.html'},
        name='password_reset_complete'),
    	
    #url(r'^$', include('apps.mascota.urls')),
]
