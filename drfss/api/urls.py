from django.conf.urls import url, include

urlpatterns = [
    url(r'^rest/', include('drfss.api.rest.urls', namespace='rest')),
]
