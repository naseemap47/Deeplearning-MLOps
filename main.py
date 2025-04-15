from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline


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
