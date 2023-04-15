## Sobhan Asasi Project

import os
import sys
from src.exception import CustomExeption
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestConfig:
    
    train_data_path: str= os.path.join('artifacts','train.csv')
    test_data_path: str= os.path.join('artifacts','test.csv')
    raw_data_path: str= os.path.join('artifacts','data.csv')    

class DataIngest:
    def __init__(self) -> None:
        self.ingest_config = DataIngestConfig()

    def initiate_data_ingestion(self):
        
        logging.info('Entered the data ingestion method')
        
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')
            
            os.makedirs(os.path.dirname(self.ingest_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingest_config.raw_data_path, index=False, header=True)
            logging.info('Train Test Split Initiated')
            
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingest_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingest_config.test_data_path, index=False, header=True)
            logging.info('Ingestion of data is completed')

            return(
                self.ingest_config.train_data_path,
                self.ingest_config.test_data_path

            )
        except Exception as e:
            raise CustomExeption(e, sys)

if __name__=="__main__":
    obj = DataIngest()
    obj.initiate_data_ingestion()