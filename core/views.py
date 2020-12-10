from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .core_service import create_product, validate_product_request, \
    get_all_products, filter_product


@api_view(['GET'])
def get_products(request):
    """ Get all product/products by product_name, product_id or owner_id."""
    if request.GET:
        response = filter_product(request.GET)
        return Response(response)
    else:
        response = get_all_products()
        return Response(response, status=status.HTTP_200_OK)


@api_view(['POST'])
def set_products(request):
    """ Insert into product model values with product_name, product_id or owner_id"""
    user_data = request.data
    validate_info = validate_product_request(user_data)
    if 'error' not in validate_info:
        product_name = user_data.get('product_name', '')
        product_id = user_data.get('product_id')
        owner_id = user_data.get('owner_id')
        response = create_product(product_name, product_id, owner_id)
        return Response(response, status=status.HTTP_200_OK)
    else:
        return Response(validate_info, status=status.HTTP_400_BAD_REQUEST)
