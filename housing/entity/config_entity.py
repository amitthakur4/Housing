from collections import namedtuple

#Imagine Vast Territories, Traverse every peak!!

#it would be downloaddir, after extraction dir, raw data dir
DataIngestionConfig= namedtuple("DataIngestionConfig",
                                ["dataset_download_url", "tgz_download_dir", "raw_data_dir", "ingested_trained_dir", "ingested_test_dir"])

#it would be no of cols and there data_types
DataValidationConfig = namedtuple(
                                  "DataValidationConfig",
                                  ["schema_file_path"]
                                  )  

# this would have keys regrding feature engineering (test and train would be after applying fe where i swill saev that data)
DataTransformationConfig = namedtuple("DataTransformationConfig", 
                                      ["add_bedroom_per_room", "transformed_train_dir", "transformed_test_dir",
                                       "preprocessed_object_file_path"])  #after tensform we pick and strore preprocessed dir is that

# when i tarin my model i will pck it so that dir will be specified along with the base accuracy
ModelTrainingConfig = namedtuple("ModelTrainingConfig",
                                 ["trained_model_file_path", "base_accuracy"])

#Every details about the model in prod will be in thi path along with the time stamp (when u r comparing train vs base - activity timestamp)
ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",
                                   ["model_evaluation_file_path", "time_stamp"])

#if train model is better than base model, we will save it somewhere ( path of that)
ModelPusherConfig = namedtuple("ModelPusherConfig", ["export_dir_path"])


TrainingPipelineConfig = namedtuple("TrainingPipelineConfig",["artifact_dir"])

