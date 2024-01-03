from housing.config.configuration import Configuration
from housing.logger import logging
from housing.exception import HousingException
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.entity.config_entity import DataIngestionConfig
from housing.components.data_ingestion import DataIntegation
import os
import sys


class Pipeline:

    def __init__(self, config: Configuration= Configuration()) -> None:
        try:
            self.config= config
        except Exception as e:
            raise HousingException(e, sys) from e

    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            data_ingestion= DataIntegation(data_ingestion_config= self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def start_data_validation(self)->None:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def start_data_transformation(self)-> None:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def start_model_trainer(self)-> None:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e
    
    def start_model_evaluation(self)-> None:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def start_model_pusher(self)-> None:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise HousingException(e,sys) from e