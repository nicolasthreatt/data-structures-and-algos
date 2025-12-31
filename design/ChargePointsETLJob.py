"""
BNSF - ETL Pipeline

Objective:
    * Create an ETL job which will read data from a file, transform it into the desired state,
      and save it to an output location.

Environment:
    * Spark version: 3.5.5
    * Python version: 3.12.10

Input:
    * File: electric-chargepoints-2017.csv (available in input_path inside ChargePointsETLJob)
    * Contains data published by the UK Department for Transport about electric vehicle charge points usage in 2017

Requirements:
    * For each charge point (CPID), calculate:
        - Longest plugin duration (hours)
        - Average plugin duration (hours)
    * Use PySpark to implement the ETL pipeline with these three methods:
        1. extract(): returns a DataFrame with raw input data.
        2. transform(df): takes raw DataFrame, returns DataFrame with columns:
            - chargepoint_id
            - max_duration
            - avg_duration
        3. load(df): saves transformed DataFrame as Parquet to output_path
    * Output:
        - One row per charge point
        - Column names: chargepoint_id, max_duration, avg_duration
        - Round numerical values to 2 decimal places

Example Input Rows:
    ChargingEvent | CPID     | StartDate   | StartTime  | EndDate     | EndTime    | Energy | PluginDuration
    15554472      | AN07263  | 2017-10-29  | 13:30:00   | 2017-10-29  | 17:08:00   | 5.3    | 3.63333333
    15329256      | AN15092  | 2017-10-14  | 17:37:00   | 2017-10-15  | 05:26:00   | 19.2   | 11.8166666
    2344473       | AN22594  | 2017-06-02  | 16:10:19   | 2017-06-03  | 13:03:21   | 11.5   | 20.8838888
    12184545      | AN10218  | 2017-03-20  | 21:43:37   | 2017-03-21  | 20:18:29   | 12.1   | 22.58111111
    11984777      | AN02137  | 2017-03-07  | 10:21:17   | 2017-03-08  | 18:10:15   | 7.8    | 31.81611111

Example Output Row:
    chargepoint_id | max_duration | avg_duration
    AN06056        | 11.98        | 4.76
"""

from pyspark.sql import DataFrame, SparkSession, functions as F, types as T


class ChargePointsETLJob:
    input_path = 'data/input/electric-chargepoints-2017.csv'
    output_path = 'data/output/chargepoints-2017-analysis'

    def __init__(self):
        self.spark_session: SparkSession = (
            SparkSession.builder
                .master("local[*]")
                .appName("ElectricChargePointsETLJob")
                .getOrCreate()
        )

    def extract(self) -> DataFrame:
        schema = T.StructType([
            T.StructField("ChargingEvent", T.IntegerType(), True),
            T.StructField("CPID", T.StringType(), True),
            T.StructField("StartDate", T.StringType(), True),
            T.StructField("StartTime", T.StringType(), True),
            T.StructField("EndDate", T.StringType(), True),
            T.StructField("EndTime", T.StringType(), True),
            T.StructField("Energy", T.DoubleType(), True),
            T.StructField("PluginDuration", T.DoubleType(), True)
        ])

        df = self.spark_session.read.csv(
            self.input_path, 
            header=True, 
            schema=schema
        )

        return df

    def transform(self, df: DataFrame) -> DataFrame:
        return (
            df.groupBy(F.col("CPID"))
                .agg(
                    F.round(F.max(F.col("PluginDuration")), 2).alias("max_duration"),
                    F.round(F.avg(F.col("PluginDuration")), 2).alias("avg_duration")
                )
                .withColumnRenamed("CPID", "chargepoint_id")
            )

    def load(self, df: DataFrame):
        df.write.mode("overwrite").parquet(self.output_path)

    def run(self):
        self.load(self.transform(self.extract()))


if __name__ == "__main__":
    job = ChargePointsETLJob()
    job.run()
