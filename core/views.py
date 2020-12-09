from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def index(request):
    data = {'username': 'Stas', 'id': 12}
    params = request.GET
    if params:
        key = params.get('key', '')
        return Response(data.get(key, {}))
    else:
        return Response(data)
