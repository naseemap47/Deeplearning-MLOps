from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline


STAGE1_NAME = "Data Ingestion Stage"

try:
    logger.info(f"> > > > > > Stage: {STAGE1_NAME} Started < < < < < <")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"> > > > > > Stage: {STAGE1_NAME} Completed < < < < < <\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise(e)


STAGE2_NAME = "Prepare Base Model"

try:
    logger.info(f"> > > > > > Stage: {STAGE2_NAME} Started < < < < < <")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f"> > > > > > Stage: {STAGE2_NAME} Completed < < < < < <\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise(e)


STAGE3_NAME = "Training"

try:
    logger.info(f"> > > > > > Stage: {STAGE3_NAME} Started < < < < < <")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f"> > > > > > Stage: {STAGE3_NAME} Completed < < < < < <")
except Exception as e:
    logger.exception(e)
    raise(e)

STAGE4_NAME = "Evaluation Stage"

try:
    logger.info(f"> > > > > > Stage: {STAGE4_NAME} Started < < < < < <")
    model_evaluation = EvaluationPipeline()
    model_evaluation.main()
    logger.info(f"> > > > > > Stage: {STAGE4_NAME} Completed < < < < < <")
except Exception as e:
    logger.exception(e)
    raise e
