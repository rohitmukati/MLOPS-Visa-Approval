from us_visa.configuration.mongo_db_connection import MongoDBClient
from us_visa.constants import DATABASE_NAME
from us_visa.exception import USvisaException
from us_visa.logger import logging
import pandas as pd 
from typing import Optional
import numpy as np
import sys



class USvisaData:
    """
    Class Name :   USvisaData
    Description :   This class is used to access the US visa data from MongoDB.
    
    Output      :   DataFrame containing US visa data
    On Failure  :   raises an exception
    """
    
    def __init__(self):
        
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise USvisaException(e, sys)
        
        
    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
                
            else:
                collection = self.mongo_client[database_name][collection_name]
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.tolist():
                df = df.drop(columns=["_id"], axis=1)
            df.replace("na", np.nan, inplace=True)
            return df
        except Exception as e:
            raise USvisaException(e, sys)
            
            