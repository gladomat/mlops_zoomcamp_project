from prefect.orion.schemas.schedules import IntervalSchedule
from datetime import timedelta
from preproc_modelling.preprocess_data import preprocessor
from preproc_modelling.model_training import trainer
from preproc_modelling.register_model import register_model_flow
from prefect import flow, Flow
from prefect.task_runners import SequentialTaskRunner


@flow(task_runner=SequentialTaskRunner())
def main_flow():
    preprocessor()
    trainer()
    register_model_flow()