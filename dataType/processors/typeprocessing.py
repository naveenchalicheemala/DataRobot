
import datetime


"""
This class includes methods to find data type of each column
"""


class TypeProcessing:

    """
    This method is used to check the type of value in the column. If it is string, it will check for Boolean and
    datetime type. Otherwise, it returns the type(val)
    """
    def checkForType(self, val):

        if (isinstance(val, str)):

            if self.checkForBoolean(val):
                return type(True).__name__
            elif self.checkForDateTime(val):
                return datetime.__name__

        return type(val).__name__


    """
    This method checks if the value is boolean. 
    """
    def checkForBoolean(self, val):

        if (("true" == val.lower()) or ("false" == val.lower())):
            return True
        else:
            return False

    """
    This method checks if the value has a datatime format. It will check for the specified formats mentioned
    """
    def checkForDateTime(self, val):

        for format in ('%Y-%m-%d', '%m-%d-%Y', '%d-%m-%Y',
                       '%d.%m.%Y', '%m.%d.%Y', '%Y.%m.%d',
                       '%d/%m/%Y', '%m/%d/%Y', '%Y/%m/%d'):
            try:
                if (type(datetime.datetime.strptime(val, format) is datetime.datetime)):
                    return True
            except ValueError:
                pass

        return False


    """ 
    This method returns the full string for each type 
    """
    def returnString(self, type):

        dataTypes = {"int": "Integer", "float": "Float", "str": "String", "bool": "Boolean", "date": "DateTime"}

        for key in dataTypes.keys():
            if key in type:
                return dataTypes[key]

        return "Not Defined"


    """
    This method compares the type of earlier values with the current one according to the below scenarios:
    1. If a column has Integer and float, the type of column would be Float.  
    2. If a column has mixed types (Integer, Float, Boolean, DateTime, String), the type would be String
    """
    def comparetype(self, old_type, new_type):

        if ((old_type == ["Integer", "Float"]) and (new_type in ["Integer", "Float"])):
            return "Float"
        elif ((old_type in ["Boolean", "Integer", "Float", "DateTime"]) and (new_type in ["String"])):
            return "String"
        elif ((old_type in ["String"]) and (new_type in ["Boolean", "Integer", "Float", "DateTime"])):
            return "String"
        elif ((old_type in ["Integer", "Float", "DateTime"]) and (new_type in ["Boolean"])):
            return "String"
        elif ((old_type in ["Integer", "Float", "Boolean"]) and (new_type in ["DateTime"])):
            return "String"
        else:
            return new_type