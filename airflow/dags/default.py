# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
from datetime import timedelta
from datetime import datetime as dt

DEFAULT_ARGS = dict(
    owner='Airflow',
    email=['h4ckcheek@gmail.com'],
    email_on_failure=False,
    email_on_retry=False,
    depends_on_past=False,
    schedule_interval='0 0 20 * *',
    start_date=dt(2022,9,6),
    # retries=2,
    # retry_delay=timedelta(minutes=5),

    # 'queue'= 'bash_queue',
    # 'pool'= 'backfill',
    # 'priority_weight'= 10,
    # 'end_date'= datetime(2016, 1, 1),
    # 'wait_for_downstream'= False,
    # 'dag'= dag,
    # 'sla'= timedelta(hours=2),
    # 'execution_timeout'= timedelta(seconds=300),
    # 'on_failure_callback'= some_function,
    # 'on_success_callback'= some_other_function,
    # 'on_retry_callback'= another_function,
    # 'sla_miss_callback'= yet_another_function,
    # 'trigger_rule'= 'all_success'
)
