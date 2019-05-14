from src.services.dtos import MIDto


class FilterMethod:

    def get_pearson_correlation(self, dataframe):
        raise NotImplementedError('You must implement this method')

    def get_mutual_information(self, variables, target) -> MIDto:
        raise NotImplementedError('You must implement this method')

    def get_anova(self,  data, dependent_variables, independent_variables):
        raise NotImplementedError('You must implement this method')

