def validate_product(product):
    required_fields = ['name', 'description', 'price', 'image']
    for field in required_fields:
        if field not in product or not product[field]:
            return False
    return True
