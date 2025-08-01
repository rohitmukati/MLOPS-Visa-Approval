import os 
from us_visa.constants import *
from dataclasses import dataclass
from datetime import datetime


TIMESTAMP = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

@dataclass
class TraningPipelineConfig:
    pipeline_name: str = PIPELINE_NAME,
    artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP),
    timstamp: str = TIMESTAMP 
 
 
    
training_pipeline_config: TraningPipelineConfig = TraningPipelineConfig()



@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir, DATA_INGESTION_DIR_NAME)
    feature_store_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME)
    training_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME)
    testing_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME)
    train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
    collection_name:str = DATA_INGESTION_COLLECTION_NAME

