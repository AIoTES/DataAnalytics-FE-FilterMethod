import json
import logging

from flask import Blueprint, request, Response
from src.services.data_lake_service import QueryDataLake

import src.utils.utils as utils
from src.services.filter_method_service import FilterMethod

api = Blueprint('selectFeatures_controller', __name__)
selectFeatures: FilterMethod = None
queryDataLake: QueryDataLake = None


@api.route('filterMethod', methods=['POST'])
def filter_method():
    data = request.get_json() or {}

    if not data:
        logging.error("{}:{}".format("ContentLengthRequired", "Zero/No Content-Length"))
        return utils.error_response(411, "Zero/No Content-Length")

    print(list(data.keys()))

    if 'method' not in list(data.keys()) or 'dataDesc' not in list(data.keys()):
        logging.error("{}:{}".format("Bad Request", "JSON Incomplete"))
        return utils.bad_request("JSON incomplete. {} fields are necessary".format(['method', 'dataDesc']))

    df = queryDataLake.retrieve_data_as_data_frame(data['dataDesc'])

    if data['method'] == 'pearson':
        message = selectFeatures.get_pearson_correlation(df)
        return Response(response=json.dumps(message), content_type="application/json", status=200)

    if data['method'] == "mutual_information":
        message = selectFeatures.get_mutual_information(df.iloc[:, 0:len(df.columns)], df.iloc[:, 0])
        return Response(response=json.dumps(message, sort_keys=True, separators=(',', ':')),
                        content_type="application/json", status=200)

    if 'anova' in data['method']:
        message = selectFeatures.get_anova(df, data['method']['anova']['dependent_variable'],
                                           data['method']['anova']['independent_variables'])
        return Response(response=json.dumps(message, sort_keys=True, separators=(',', ':')),
                        content_type="application/json", status=200)


@api.route('/wrapperMethod', methods=['GET'])
def wrapper_method():
    # TODO: Quedaría por implementar esto entero. Existen librerías de python para hacer el wrapper,
    #  pero no contemplan el clustering Si dan mucho follón los de Grecia diría de escoger un listado de técnicas y
    #  decir que solo se puede hacer el wrapper con ellas En la petición deberían pasar tanto la técnica como los
    #  valores de los hiperparámetros y el conjunto de datos clasificado
    wrapper = None
