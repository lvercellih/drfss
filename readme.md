# drfss (django rest framework static schema)

Una forma simple de usar un esquema estático con
[django-rest-framework](https://github.com/tomchristie/django-rest-framework) y
[django-rest-swagger](https://github.com/marcgibbons/django-rest-swagger)

## Pasos

- Crear una clase que renderize `json` pero que reconozca el formato `openapi`

```python
from rest_framework.renderers import JSONRenderer


class JSONOpenAPIRenderer(JSONRenderer):
    format = 'openapi'
```

- Crear la vista que que retornará el swagger ui

```python
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_swagger.renderers import SwaggerUIRenderer


class SwaggerSchemaView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [
        SwaggerUIRenderer,
        JSONOpenAPIRenderer
    ]

    def get(self, request):
        return Response(schema)

```

- Colocar en la variable `schema` un `dict` conteniendo el schema `openapi` para que sea devuelto en json

> Ver el ejemplo completo en el archivo [drfss/api/rest/views.py](drfss/api/rest/views.py)

> En el ejemplo se está usando el api de instagram, obtenido de http://editor.swagger.io/

