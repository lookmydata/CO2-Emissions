from pyspark.sql import SparkSession
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.utils import AnalysisException


def spark_session() -> SparkSession:

    if SparkSession.getActiveSession():
        return SparkSession.getActiveSession()

    else:
        spark: SparkSession = (
            SparkSession.builder.master("local")
            .appName("CO2_Emissions")
            .config("spark.driver.host", "127.0.0.1")
            .config("spark.driver.bindAddress", "127.0.0.1")
            .config("spark.ui.port", "4040")
            .getOrCreate()
        )
        return spark


def updata(spark: SparkSession, path: str, name: str) -> DataFrame:
    """
    Usage
    >>> spark = spark_session
    >>> df = updata(spark, 'datasets/data.csv', data)
    """

    data: DataFrame = spark.read.csv(
        path,
        header=True,
    )

    try:
        spark.sql(f"SELECT * FROM {name}")

    except AnalysisException:
        data.registerTempTable(name)

    return data
