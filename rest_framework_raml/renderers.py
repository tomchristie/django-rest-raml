from raml_codec import RAMLCodec
from rest_framework.renderers import BaseRenderer
from django.shortcuts import render


class RAMLDocsRenderer(BaseRenderer):
    media_type = 'text/html'
    format = 'html'
    template = 'rest_framework_raml/index.html'
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        request = renderer_context['request']
        return render(request, self.template)


class RAMLRenderer(BaseRenderer):
    media_type = 'application/raml+yaml'
    format = 'raml'
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        codec = RAMLCodec()
        return codec.encode(data)
