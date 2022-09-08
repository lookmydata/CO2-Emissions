from airflow.operators.bash_operator import BashOperator
from airflow.sensors.external_task import ExternalTaskSensor
from airflow import DAG
from default import DEFAULT_ARGS
 

with DAG(
    'Push to git',
    default_args=DEFAULT_ARGS
) as dag:

    ETL_dag_success = ExternalTaskSensor(
        task_id="downstream_task1",
        external_dag_id='ETL',
        external_task_id=None,
        allowed_states=['success'],
        failed_states=['failed', 'skipped']
    )

    git_push = BashOperator(
        task_id='git_push',
        bash_command="scripts/airflow_git_push.sh"
    )

    ETL_dag_success >> git_push
