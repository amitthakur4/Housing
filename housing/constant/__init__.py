import os
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.getcwd()))

CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"  

########################---- KEY-> present in yaml  DIR-> folder name  ###############################

#training pipeline realted varibaler 
TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"

#data ingestion related variable
DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = "tgz_download_dir"
DATA_INGESTION_DIR_NAME_KEY = "ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY = "ingested_test_dir"


#data validation related variable
DATA_VALIDATION_CONFIG_KEY = "data_validation_config"
DATA_VALIDATION_ARTIFACT_DIR = "data_validation"
DATA_VALIDATION_SCHEMA_DIR = "schema_dir"
DATA_VALIDATION_REPORT_FINE_NAME = "report.json"
DATA_VALIDATION_SCHEMA_FILE_NAME = "schema.yaml"
DATA_VALIDATION_REPORT_PAGE_FILE_NAME = "report.html"


#data transformation config
DATA_TRANSFORMATION_CONFIG_KEY = "data_transformation_config"
DATA_TRANSFORMATION_ARTIFACT_DIR =  "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DIR = "transformed_data"
DATA_TRANSFORMATION_TRANSFORMED_TRAIN_DIR = "train"
DATA_TRANSFORMATION_TRANSFORMED_TEST_DIR = "test"
DATA_TRANSFORMATION_PREPROCESSING_DIR = "preprocessed"
DATA_TRANSFORMATION_PREPROCESSING_OBJECT_FILENAME = "preprocessed.pkl"

#model traner config
MODEL_TRAINER_CONFIG_KEY = "model_trainer_config"
MODEL_TRAINER_ARTIFACT_DIR = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR= "trained_model_dir"
MODEL_TRAINER_MODEL_FILE_NAME= "model_file_name"
MODEL_TRAINER_BASE_ACCURACY= "base_accuracy"
MODEL_TRAINER_CONFIG_DIR= "model_config_dir"
MODEL_TRAINER_CONFIG_FILE_NAME= "model_config_file_name"

#model_evaluation_config
MODEL_EVALUATION_CONFIG_KEY = "model_evaluation_config"
MODEL_EVALUATION_ARTIFACT_DIR = "model_evaluation"
MODEL_EVALUATION_FILE_NAME = "model_evaluation_file_name"

# model pusher related config
MODEL_PUSHER_CONFIG_KEY = "model_pusher_config"
MODEL_PUSHER_ARTIFACT_DIR = "model_pusher"
MODEL_PUSHER_EXPORT_DIR = "model_export_dir"








