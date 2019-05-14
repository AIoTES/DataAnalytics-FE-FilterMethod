import unittest
import pandas as pd

from src.services.dtos import MIDto
from src.services.filter_method_impl import FilterMethodImpl


class TestFilterMethodService(unittest.TestCase):

    def setUp(self):
        self.filter_method_service = FilterMethodImpl()
        self.test_mi = MIDto([0.39791001693573813, 3.48206273179784])
        self.test_pearson = {
            'Working Electrode NO2': {'Working Electrode NO2': 1.0, 'Auxiliar Electrode NO2': 0.6440846343974541},
            'Auxiliar Electrode NO2': {'Working Electrode NO2': 0.6440846343974541, 'Auxiliar Electrode NO2': 1.0}}

    def test_mutual_information(self):
        df = pd.read_csv('../../resources/dataset.csv', delimiter=';', index_col=0)

        result = self.filter_method_service.get_mutual_information(df.iloc[:, 0:2], df.iloc[:, 1])
        print(df.iloc[:, 0:2])
        print(df.iloc[:, 1])
        self.assertEqual(self.test_mi.to_dict(), result)

    def test_pearson(self):
        df = pd.read_csv('../../resources/dataset.csv', delimiter=';', index_col=0)

        result = self.filter_method_service.get_pearson_correlation(df.iloc[:, 0:2])
        self.assertEqual(self.test_pearson, result)

    def test_anova(self):
        df = pd.read_csv('../../resources/dataset.csv', delimiter=';')

        result = self.filter_method_service.get_anova(data=df, dependent_variable='Working Electrode NO2',
                                                      independent_variables=['Auxiliar Electrode NO2'])
        self.assertEquals({'p-value': 2.071575699111506e-09}, result)