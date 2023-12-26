##where are you from data read,train_test_split

import os
import sys
from src.logger import logging
from src.exception import CustomException   #src in exception present
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


## intialize the data ingestion configuration

@dataclass   #used @datasclass so that don't hato to make initialize constructor
class DataIngestionconfig:
    #without using any self keyword make parameter(class variable)
    train_data_path=os.path.join('artifacts','train.csv')   #train file save in artifacts,filename
    test_data_path=os.path.join('artifacts','test.csv')
    raw_data_path=os.path.join('artifacts','raw.csv')   #read data save in this file beacuse repeatedly data read is costly


## create a data ingestion class(for used data read,train_test_split)
class DataIngestion:      
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()  #come parameter train,test,raw

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion method starts')

        try:    #data read
            df=pd.read_csv(os.path.join('notebooks/data','gemstone.csv'))
            logging.info('Dataset read as pandas Dataframe')

            #code through artifatcts folder
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)

            #raw data save in csv file
            df.to_csv(self.ingestion_config.raw_data_path,index=False)

            logging.info("Train test split")
            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)

                  #save train_set,test_set in folder location
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of data is completed')

            return(         #data transformation here to read and perform feature engineering
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )



        except Exception as e:
            logging.info('Error occured in Data Ingestion config')








