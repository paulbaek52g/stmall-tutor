from flask import Flask, abort, jsonify, request, Blueprint, Response
import ProductRepository 
import Hateoas 

bp = Blueprint('product', __name__, url_prefix='/products')

@bp.route("", methods=["POST"])
def Post():
    response = ProductRepository.Create(request)

    response = Hateoas.POST_response(request.base_url, response)
    return response

@bp.route("", methods=["GET"])
def Get():
    response = ProductRepository.Read(request)
    response = Hateoas.GET_list_response(request.url_root, request.base_url, response)
    
    return response

@bp.route("/<int:id>", methods=["GET"])
def Get_By_Id(id: int):
    response = ProductRepository.Read_by_id(id)

    if response != 'error':
        response = Hateoas.GET_id_response(request.base_url, response)
    else:
        response = Response(response, status=404,mimetype='application/json')
    return response

@bp.route("/<int:id>", methods=["UPDATE"])
def Update(id: int):
    
    response = ProductRepository.Update(id, request)
    
    if response != 'error':
        response = Hateoas.GET_id_response(request.base_url, response)
    else:
        response = Response(response, status=403,mimetype='application/json')

    
    return response

@bp.route("/<int:id>", methods=["DELETE"])
def Delete(id: int):
    response = ProductRepository.Delete(id)
    if response == None:
        response = Response(status=200, mimetype='application/json')
    else :
        response = Response(response, status=403,mimetype='application/json')
    
    return response


@bp.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404
