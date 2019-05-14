import pandas as pd


class QueryDataLake:

    def retrieve_data_as_data_frame(self, dataDesc):
        if "query" in dataDesc:
            print("Query to data lake not implemented returning default values. Query: " + dataDesc["query"])
            return pd.read_csv('../resources/dataset.csv', delimiter=';', index_col=0)

        if "expression" in dataDesc:
            expression_splitted = dataDesc["expression"].split()
            if len(expression_splitted) == 1:
                for element in dataDesc["data"]:
                    delete = [key for key in element if key != expression_splitted[0]]
                    for key in delete: del element[key]

            else:
                for element in dataDesc["data"]:
                    result = []
                    for x in range(0, len(element[expression_splitted[0]])):
                        if expression_splitted[1] == '*':
                            result.append(element[expression_splitted[0]][x] * element[expression_splitted[2]][x])
                        elif expression_splitted[1] == '/':
                            result.append(element[expression_splitted[0]][x] / element[expression_splitted[2]][x])
                        elif expression_splitted[1] == '+':
                            result.append(element[expression_splitted[0]][x] + element[expression_splitted[2]][x])
                        elif expression_splitted[1] == '-':
                            result.append(element[expression_splitted[0]][x] - element[expression_splitted[2]][x])

                    element["result"] = result

                for element in dataDesc["data"]:
                    delete = [key for key in element if key != "result"]
                    for key in delete: del element[key]

        if len(dataDesc["data"]) == 1:
            df_response = pd.DataFrame.from_dict(dataDesc["data"][0])
        else:
            expression_splitted = dataDesc["expression"].split()
            if len(expression_splitted) == 1:

                df_response = [dataDesc["data"][0][expression_splitted[0]]]
                for x in range(1, len(dataDesc["data"])):
                    df_response = pd.np.concatenate((df_response, [dataDesc["data"][x][expression_splitted[0]]]))
            else:
                df_response = [dataDesc["data"][0]["result"]]
                for x in range(1, len(dataDesc["data"])):
                    df_response = pd.np.concatenate((df_response, [dataDesc["data"][x]["result"]]))

        return df_response
