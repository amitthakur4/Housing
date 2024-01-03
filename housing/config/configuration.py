from housing.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, \
    ModelTrainingConfig, ModelEvaluationConfig, ModelPusherConfig, TrainingPipelineConfig
from housing.util.util import read_yaml_file
from housing.logger import logging
import os
from housing.constant import *
import sys
from housing.exception import HousingException


# ROOT_DIR = os.getcwd()  #rather than creating constant here we will creates file where ll specify all constants


class Configuration:

    def __init__(self,
                 config_file_path=CONFIG_FILE_PATH,
                 current_time_stamp: str = CURRENT_TIME_STAMP,
                 ) -> None:
        print("-------------------", config_file_path)
        try:
            self.config_info = read_yaml_file(config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.current_time_stamp = CURRENT_TIME_STAMP
        except Exception as e:
            raise HousingException(e, sys) from e

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_ingestion_artifact_dir = os.path.join(artifact_dir,
                                                       DATA_INGESTION_ARTIFACT_DIR,
                                                       self.current_time_stamp
                                                       )
            data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]
            dataset_download_url = data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY]
            tgz_download_dir = os.path.join(artifact_dir,
                                            data_ingestion_info[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY],
                                            self.current_time_stamp
                                            )
            raw_data_dir = os.path.join(data_ingestion_artifact_dir,
                                        data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY]
                                        )
            ingested_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_DIR_NAME_KEY]
            )
            ingested_trained_dir = os.path.join(ingested_data_dir,
                                                data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY])
            ingested_test_dir = os.path.join(ingested_data_dir,
                                             data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY])

            data_ingestion_config = DataIngestionConfig(
                dataset_download_url=dataset_download_url,
                tgz_download_dir=tgz_download_dir,
                raw_data_dir=raw_data_dir,
                ingested_trained_dir=ingested_trained_dir,
                ingested_test_dir=ingested_test_dir
            )
            return data_ingestion_config
        except Exception as e:
            raise HousingException(e, sys) from e

    def get_data_vaildation_config(self) -> DataValidationConfig:
        artifact_dir = self.training_pipeline_config.artifact_dir
        data_validation_artifact_dir = os.path.join(artifact_dir,
                                                    DATA_VALIDATION_CONFIG_KEY,
                                                    self.current_time_stamp
                                                    )
        data_ingestion_info = self.config_info[DATA_VALIDATION_CONFIG_KEY]
        pass

    def get_data_transformation_config(self) -> DataTransformationConfig:
        artifact_dir = self.training_pipeline_config.artifact_dir
        data_validation_artifact_dir = os.path.join(artifact_dir,
                                                    DATA_VALIDATION_CONFIG_KEY,
                                                    self.current_time_stamp
                                                    )
        data_ingestion_info = self.config_info[DATA_VALIDATION_CONFIG_KEY]

    def get_data_trainer_config(self) -> ModelTrainingConfig:
        artifact_dir = self.training_pipeline_config.artifact_dir
        data_validation_artifact_dir = os.path.join(artifact_dir,
                                                    DATA_VALIDATION_CONFIG_KEY,
                                                    self.current_time_stamp
                                                    )
        data_ingestion_info = self.config_info[DATA_VALIDATION_CONFIG_KEY]

    def get_data_evaluation_config(self) -> ModelEvaluationConfig:
        artifact_dir = self.training_pipeline_config.artifact_dir
        data_validation_artifact_dir = os.path.join(artifact_dir,
                                                    DATA_VALIDATION_CONFIG_KEY,
                                                    self.current_time_stamp
                                                    )
        data_ingestion_info = self.config_info[DATA_VALIDATION_CONFIG_KEY]

    def get_data_pusher_config(self) -> ModelPusherConfig:
        artifact_dir = self.training_pipeline_config.artifact_dir
        data_validation_artifact_dir = os.path.join(artifact_dir,
                                                    DATA_VALIDATION_CONFIG_KEY,
                                                    self.current_time_stamp
                                                    )
        data_ingestion_info = self.config_info[DATA_VALIDATION_CONFIG_KEY]

    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]  # got dict from yaml file
            artifact_dir = os.path.join(
                ROOT_DIR, training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
                training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )
            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training pipeline config: {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise HousingException(e, sys) from e


if __name__ == "__main__":
    obj = Configuration()
    obj.get_data_ingestion_config()
