from flask import Blueprint, render_template, redirect, url_for, request, jsonify
import fetch.main.resource as resource
import json

def GET_PRODUCT():
    '''
    Get all product with price IDR attribute.

    Returns
    ----------
    product : list
        a list of product
    '''

    product = json.loads(resource.GET_PRODUCT_RESOURCE())
    idr_from_usd = json.loads(resource.GET_IDR_FROM_USD())
    idr_from_usd = idr_from_usd['USD_IDR']

    for item in product:
        item['price_idr'] = float(item['price'])  * idr_from_usd

    return json.dumps(product)

def GET_AGGREGATED_PRODUCT():
    '''
    Get all product with aggregated by department, product, and price idr. Also ordered by price ascending.

    Returns
    ----------
    sorted_product : list
        a list of product that sorted by price
    '''

    product = json.loads(resource.GET_PRODUCT_RESOURCE())
    idr_from_usd = json.loads(resource.GET_IDR_FROM_USD())
    idr_from_usd = idr_from_usd['USD_IDR']

    aggregated_product = []
    for item in product:
        aggregated_product.append({
            "department": item['department'],
            "product": item['product'],
            "price_idr": float(item['price'])  * idr_from_usd,
            "price": item['price']
        })
    
    sorted_product = sorted(aggregated_product, key=lambda x : x['price'], reverse=False)

    return json.dumps(sorted_product)

