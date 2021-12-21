from flask import Blueprint, render_template, redirect, url_for, request, jsonify
import os
import requests

def GET_PRODUCT_RESOURCE():
    product_resource_url = os.environ.get('PRODUCT_RESOURCE_URL')

    r = requests.get(product_resource_url)
    return r.content

def GET_IDR_FROM_USD():
    idr_from_usd = os.environ.get('CONVERTER_USD_TO_IDR_URL')

    r = requests.get(idr_from_usd)
    return r.content