""" Service for manage work with Django models. """
from .models import ProductOwner, Product

PRODUCT_ARGUMENTS = ('product_name', 'product_id', 'owner_id')


def _create_product(product_name, product_id, owner_id, owner) -> dict:
    """ Get or create new product from Database.

    :param product_name: name for new product.
    :param product_id:   id for new product.
    :param owner_id:     id of existing product owner.
    :param owner:        owner instances.
    :return:             message with creation status.
    """
    if owner:
        obj, created = Product.objects.get_or_create(product_name=product_name,
                                                     product_id=product_id,
                                                     owner_id=owner[0])
        if created:
            return {'message': f'Product with name {product_name} was created'}
        else:
            return {'message': f'This product already in DB'}
    else:
        return {'message': f'No owner with {owner_id} in DB'}


def get_owner_by_id(owner_id) -> list:
    """ Get product owner by owner_id.
    
    :param owner_id: id of existing product owner.
    :return:         list with owners instances.
    """
    owner = ProductOwner.objects.filter(owner_id=owner_id)
    return owner


def _form_filter(request: dict) -> dict:
    """ Form filter request.
    
    :param request: HTTP requests.
    :return:        dict with param for request in models.
    """
    filters = {}
    for argument in PRODUCT_ARGUMENTS:
        if request.get(argument):
            filters[argument] = request.get(argument)
    return filters


def create_product(product_name: str, product_id: int, owner_id: int) -> dict:
    """ Create product by product_name, product_id and owner_id.

    :param product_name: name for new product.
    :param product_id:   id for new product.
    :param owner_id:     id of existing product owner.
    :return:             message with creation status.
    """
    owner = get_owner_by_id(owner_id)
    return _create_product(product_name, product_id, owner_id, owner)


def validate_product_request(request: dict) -> dict:
    """ Validate HTTP requests for new product saving.

    :param request: HTTP requests.
    :return:        error message/ok message.
    """
    for argument in PRODUCT_ARGUMENTS:
        if not request.get(argument):
            return {'message': f'{argument} not in request', 'error': True, 'code': 400}
    return {'message': 'OK', 'code': 200}


def form_filter(request: dict) -> dict:
    """ Form filter for getting filtered products.

    :param request: HTTP requests.
    :return:        filter arguments.
    """
    arguments = _form_filter(request)
    if 'owner_id' in arguments:
        owner = get_owner_by_id(arguments.get('owner_id'))
        if owner:
            arguments['owner_id'] = owner[0]
    return arguments


def filter_product(request: dict) -> list:
    """ Get products by filters (product_name, product_id, owner_id)

    :param request: HTTP requests.
    :return:        list with filtered products.
    """
    arguments = form_filter(request)
    products = Product.objects.filter(**arguments)
    response = []
    for product in products:
        data = {
            'product_name': product.product_name,
            'product_id': product.product_id,
            'owner_id': product.owner_id.owner_id,
        }
        response.append(data)
    return response


def get_all_products() -> list:
    """ Get list with all product fields.

    :return: list of all products.
    """
    response = []
    for product in Product.objects.all():
        data = {
            'product_name': product.product_name,
            'product_id': product.product_id,
            'owner_id': product.owner_id.owner_id,
        }
        response.append(data)
    return response
