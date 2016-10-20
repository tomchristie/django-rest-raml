# Django REST RAML

**RAML Documentation Generator for Django REST framework**

[![travis-image]][travis]
[![pypi-image]][pypi]

This package offers preliminary support for RAML documentation
using Django REST framework.

![RAML Image](images/raml.png)

## Installation

Install using pip:

    $ pip install django-rest-raml

Add `'rest_framework_raml'` to your `INSTALLED_APPS` setting:

    INSTALLED_APPS = [
        ...
        'rest_framework_raml'
    ]

Include the schema view in your URL conf:

```py
from rest_framework.schemas import get_schema_view
from rest_framework_raml.renderers import RAMLRenderer, RAMLDocsRenderer

schema_view = get_schema_view(
    title='Example API',
    renderer_classes=[RAMLRenderer, RAMLDocsRenderer]
)

urlpatterns = [
    url(r'^raml/$', schema_view),
    ...
]
```

## Limitations

`django-rest-raml` does not yet support request body parameters, or response examples.

[travis-image]: https://secure.travis-ci.org/tomchristie/django-rest-raml.svg?branch=master
[travis]: http://travis-ci.org/tomchristie/django-rest-raml?branch=master
[pypi-image]: https://img.shields.io/pypi/v/django-rest-raml.svg
[pypi]: https://pypi.python.org/pypi/django-rest-raml
