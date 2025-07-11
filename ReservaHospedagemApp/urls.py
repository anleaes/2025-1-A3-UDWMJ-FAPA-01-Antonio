"""
URL configuration for ReservaHospedagemApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('anfitriao/', include('anfitriao.urls', namespace='anfitrioes')),
    path('hospede/', include('hospede.urls', namespace='hospedes')),
    path('contas/', include('accounts.urls', namespace='accounts')),
    path('imovel/', include('imovel.urls', namespace='imovel')),
    path('comodidade/', include('comodidade.urls', namespace='comodidade')),
    path('servico_adicional/', include('servico_adicional.urls', namespace='servico_adicional')),
    path('item_reserva/', include('item_reserva.urls', namespace='item_reserva')),
    path('reserva/', include('reserva.urls', namespace= 'reserva')),
    path('comodidade_imovel/', include('comodidade_imovel.urls', namespace= 'comodidade_imovel')),
    path('avaliacao/', include('avaliacao.urls', namespace= 'avaliacao')),
    path('pagamento/', include('pagamento.urls', namespace= 'pagamento')),
    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)