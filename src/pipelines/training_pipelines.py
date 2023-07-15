import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd


if __name__=='__main__':
    obj=DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()
    