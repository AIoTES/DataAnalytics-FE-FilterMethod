import sklearn.feature_selection
from src.mappers import mapper
from src.services.filter_method_service import FilterMethod
import scipy.stats as stats


class FilterMethodImpl(FilterMethod):

    def get_pearson_correlation(self, data):
        corr = data.corr()
        corr_dict = corr.to_dict()
        return corr_dict

    def get_mutual_information(self, x, y):
        mi = sklearn.feature_selection.mutual_info_regression(x, y, random_state=1)
        return mapper.mi_to_dto(mi).to_dict()

    def get_anova(self, data, dependent_variable, independent_variables):
        attributes = [dependent_variable]
        attributes = attributes + independent_variables
        statistics, pvalue = stats.f_oneway(*[data[col] for col in attributes])
        return {"p-value": pvalue}

# df = pd.read_csv('/home/hop/Escritorio/dataset.csv', delimiter=',', index_col=0)

# get_pearson_correlation(df)

# print(df.iloc[:, 2])
# result = mutual_information(df.iloc[:, 0:2], df.iloc[:, 1])

# print(result)
