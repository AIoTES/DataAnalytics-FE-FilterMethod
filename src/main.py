from flask import Flask

from src import settings
from src.controllers import selectFeatures_controller
from src.services.data_lake_service import QueryDataLake
from src.services.filter_method_impl import FilterMethodImpl

application = Flask(__name__)

filter_service = FilterMethodImpl()
data_lake_service = QueryDataLake()

selectFeatures_controller.selectFeatures = filter_service
selectFeatures_controller.queryDataLake = data_lake_service

application.register_blueprint(selectFeatures_controller.api, url_prefix='/selectFeatures')

if __name__ == '__main__':
    application.run(settings.REST_URL, settings.REST_PORT)
