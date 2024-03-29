from housing.entity.config_entity import DataIngestionConfig
from housing.logger import logging
from housing.exception import HousingException
import sys
from housing.entity.artifact_entity import DataIngestionArtifact
import tarfile
# from six.moves import urllib
import urllib.request
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit


class DataIntegation:

    def __init__(self, data_integration_config: DataIngestionConfig):
        try:
            logging.info(f"{'=' * 20} data ingestion config started {'=' * 20}")
            self.data_integration_config = data_integration_config
        except Exception as e:
            raise HousingException(e, sys) from e

    def download_housing_data(self) -> str:
        try:
            # extracting remote url to download dataset
            download_url = self.data_integration_config.dataset_download_url

            # extract folder location
            tgz_download_dir = self.data_integration_config.tgz_download_dir

            if os.path.exists(tgz_download_dir):
                os.remove(tgz_download_dir)

            os.makedirs(tgz_download_dir, exist_ok=True)

            housing_file_name = os.path.basename(download_url)
            tgz_file_path = os.path.join(tgz_download_dir, housing_file_name)

            logging.info(f"downloading file from {download_url} into : {tgz_file_path}")
            urllib.request.urlretrieve(download_url, tgz_file_path)
            logging.info(f"file [{tgz_file_path}] has been download succesfully")
            return tgz_file_path

        except Exception as e:
            raise HousingException(e, sys) from e

    def extract_tgz_file(self, tgz_file_path: str):
        try:
            raw_data_dir = self.data_integration_config.raw_data_dir

            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)

            os.makedirs(raw_data_dir)

            logging.info(f"Extracting tgz file : [{tgz_file_path}] into dir: [{raw_data_dir}]")
            with tarfile.open(tgz_file_path) as housing_tgz_file_obj:
                housing_tgz_file_obj.extractall(path=raw_data_dir)
        except Exception as e:
            raise HousingException(e, sys) from e

    def split_data_as_train_test(self):
        try:
            raw_data_dir = self.data_integration_config.raw_data_dir
            file_name = os.listdir(raw_data_dir)[0]

            housing_file_path = os.path.join(raw_data_dir, file_name)

            housing_data_frame = pd.read_csv(housing_file_path)

            housing_data_frame["income_cat"] = pd.cut(
                housing_data_frame["median_income"],
                bins=[0, 1.5, 3.0, 4.5, 6, np.inf],
                labels=[1, 2, 3, 4, 5]
            )

            strat_train_set = None
            strat_test_set = None

            split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=0.2)

            for train_index, test_index in split.split(housing_data_frame, housing_data_frame["income_cat"]):
                strat_train_set = housing_data_frame.loc[train_index].drop(["income_cat"], axis=1)
                strat_test_set = housing_data_frame.loc[train_index].drop(["income_cat"], axis=1)

            train_file_path = os.path.join(self.data_integration_config.ingested_test_dir, file_name)
            test_file_path = os.path.join(self.data_integration_config.ingested_test_dir, file_name)

            if strat_train_set is not None:
                os.makedirs(self.data_integration_config.ingested_trained_dir, exist_ok=True)
                strat_train_set.to_csv(train_file_path, index=False)

            if strat_test_set is not None:
                os.makedirs(self.data_integration_config.ingested_test_dir, exist_ok=True)
                strat_test_set.to_csv(test_file_path, index=False)

            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,
                                                            test_file_path=test_file_path,
                                                            is_ingested=True,
                                                            message=f"Data ingestion completed successfully."
                                                            )
            return data_ingestion_artifact
        except Exception as e:
            raise HousingException(e, sys) from e

    # so for this DataIngestionArtifact we again need to define it in by making artifact_entity.py
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            tgz_file_path = self.download_housing_data()
            self.extract_tgz_file(tgz_file_path=tgz_file_path)
            return self.split_data_as_train_test()
        except Exception as e:
            raise HousingException(e, sys) from e

    def __del__(self):
        logging.info(f"{'=' * 20} Data Ingestion log completed.{'=' * 20} \n\n ")
