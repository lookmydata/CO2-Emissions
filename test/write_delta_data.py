import yaml
import delta

from pyspark.sql import SparkSession


builder = (
    SparkSession
    .builder
    .appName("Test delta")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") 
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
) 
spark = delta.configure_spark_with_delta_pip(builder).getOrCreate()


with open('../datasets/data.yaml') as file:
    metadata = yaml.load(file, Loader=yaml.loader.SafeLoader)

for name, values in metadata.items():
    path = "../datasets/" + values['dir'] + values['file']
    data = spark.read.csv(path, header=True)
    (
        data
        .write
        .format("delta")
        .mode('overwrite')
        .option('overwriteSchema','true')
        .option('delta.columnMapping.mode', 'name')
        .option('delta.minReaderVersion', '2')
        .option('delta.minWriterVersion', '5')
        .save(f"../s3/{name}")
    )
