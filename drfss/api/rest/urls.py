from django.conf.urls import url

from drfss.api.rest import views

urlpatterns = [
    url(r'^$', views.SwaggerSchemaView.as_view(), name='swagger'),
]
