import os
import re

import gspread
import pandas as pd
from django import forms
from oauth2client.service_account import ServiceAccountCredentials

from dataType.processors.typeprocessing import TypeProcessing

typeProcessing = TypeProcessing()


""" 
This class is to process the user input (Sheet url and sheet name). Google sheets API is used to retrieve data from 
sheets. The API needs credentials JSON file (which is created by adding the key to service account on API) to authorize 
the access to google sheets. The sheet key is extracted from the url and processed using key and sheet name 

"""
    
class UrlProcessing:

    def processurl(self, sheetUrl, sheetName):

        result = {}

        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        DIRNAME = os.path.dirname(__file__)
        creds = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(DIRNAME, '../credentials.json'), scope)
        client = gspread.authorize(creds)

        # Create a DataFrame
        try:

            # Regular expression to extract key from google sheet url by getting the part after /d
            # Ex: (https://docs.google.com/spreadsheets/d/1fbGSEzTdLtSHW1aeo2kCv-DH7nOQThLcP7xcM_SnBXg/edit?usp=sharing

            regex = "\\/d\\/(.*?)(\\/|$)";
            sheetId = re.findall(regex, sheetUrl)
            client.login()
            worksheet = client.open_by_key(sheetId[0][0]).worksheet(sheetName)
            df = pd.DataFrame(worksheet.get_all_records())

            if df.empty:
                raise forms.ValidationError("Sheet is empty")

            # Iterate through each column to find data type for each column
            for (columnName, columnData) in df.iteritems():
                for val in columnData.values:

                    if ((columnName not in result.keys()) and (not pd.isna(val)) and (val != '')):
                        result[columnName] = typeProcessing.returnString(typeProcessing.checkForType(val))

                    elif ((columnName in result.keys()) and (typeProcessing.returnString(type(val).__name__) != result[columnName])
                          and (not pd.isna(val)) and (val != '')):
                        new_type = typeProcessing.returnString(typeProcessing.checkForType(val))
                        result[columnName] = typeProcessing.comparetype(result[columnName], new_type)

                if (columnName not in result.keys()):
                    result[columnName] = "Not Defined"

        # Below exceptions are thrown while opening the sheet
        except (ValueError, gspread.exceptions.WorksheetNotFound) as e:
            raise forms.ValidationError("Invalid Sheet Name")

        # Below exception is thrown when url is not valid
        except gspread.exceptions.APIError:
            raise forms.ValidationError("Invalid url")

        return result