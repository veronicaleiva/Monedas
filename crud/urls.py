from django.conf.urls import url
from .views import index
from .views import editar
from .views import nuevo
from .views import eliminar

urlpatterns = [
    url(r'^$', index, name='crudindex'),
    url(r'^nuevo$', nuevo, name='crudnuevo' ),
    url(r'^editar/(?P<pk>[0-9]+)$', editar, name='crudeditar' ),
    url(r'^eliminar/(?P<pk>[0-9]+)$', eliminar, name='crudeliminar' ),
]
