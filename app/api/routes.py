from flask import Blueprint,request, json

from ..models import Bikes

api = Blueprint('api', __name__,url_prefix='/api')


@api.get('/bike')
def get_bike():
    bike = Bikes.query.all()
    bike_list = [b.to_dic() for b in bike]
    return {
        'status' : 'ok',
        'bike' : bike_list
    }








