from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from flask_cors import cross_origin
import json
import fetch.main.fetch as fetch
from flask_jwt_extended import *

main = Blueprint('main', __name__)
api = "/api/v1"

@main.route(api + "/product", methods=['GET'])
@jwt_required()
def GET_PRODUCT():
    return fetch.GET_PRODUCT()

@main.route(api + "/auth", methods=['GET'])
@jwt_required()
def AUTHENTICATE_JWT():
    return jsonify(get_jwt())

@main.route(api + "/aggregated-product", methods=['GET'])
@jwt_required()
def GET_AGGREGATED_PRODUCT():
    return fetch.GET_AGGREGATED_PRODUCT()