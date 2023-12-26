
#data_ingestion
import sys
import os
from src.logger import logging
# logging.info("get started")
from src.exception import CustomException #src in exception present
import pandas as pd 

from src.components.data_ingestion import DataIngestion

from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer   #for used model trainer

if __name__=='__main__':
    logging.info("get started")
    obj=DataIngestion()  #DataIngestion path is found
    logging.info("log is started")
    train_data_path,test_data_path=obj.initiate_data_ingestion()  #return train and test_data_path
    print(train_data_path,test_data_path)


    #data transformation

    data_transformation=DataTransformation()

    # _ is object but not important
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)

    #model trainer using traning pipeline
    model_trainer=ModelTrainer()
    model_trainer.initate_model_training(train_arr,test_arr)

    
