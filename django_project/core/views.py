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
        return Response(response, status=status.HTTP_200_OK)
    else:
        response = get_all_products()
        return Response(response, status=status.HTTP_200_OK)


@api_view(['POST'])
def set_product(request):
    """ Insert into product model values with product_name, product_id or owner_id"""
    validate_info = validate_product_request(request.data)
    if 'error' not in validate_info:
        response = create_product(request.data)
        return Response(response, status=status.HTTP_201_CREATED)
    else:
        return Response(validate_info, status=status.HTTP_400_BAD_REQUEST)
