import delta
import os

from pyspark.sql import SparkSession


builder = (
    SparkSession
    .builder
    .appName("Test delta")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") 
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
) 
spark = delta.configure_spark_with_delta_pip(builder).getOrCreate()


os.chdir("../s3")
dirs = [file for file in os.listdir(".") if os.path.isdir(file)]

for dir in dirs:
    path = os.path.join("../s3", dir)
    data = (
        spark
        .read
        .format("delta")
        .option('overwriteSchema','true')
        .option('delta.columnMapping.mode', 'name')
        .option('delta.minReaderVersion', '2')
        .option('delta.minWriterVersion', '5')
        .load(path)
    )
    print('\n', dir)
    data.show(2, vertical=True)
