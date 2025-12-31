"""
BNSF - Group and sort data using PySpark.

Requirements
    - You are given a path to a file of comma-separated values (CSV), jobs.csv,
      which contains people's names and job titles, such as Dancer, Nurse, Pilot, etc.
    - The dataset has two columns: 'name' (a string data type) and job' (also a string data type).

Implement a group_sort(input_path) method that reads data from jobs.csv and returns a dictionary with job counts.

The dictionary should be ordered by count (in ascending order), then job (in ascending order from A to Z).

The group_sort (input_path) method takes one argument: input_path - a path to the CSV file containing the data.

Examples:
    - Calling the group_sort (input_path) method should return a dictionary with the following structure:
        (' Job_title_1': count_job_1, 'Job_title_2': count_job_2, ••, 'Job_title_3': count_job_3}
"""

from typing import Dict, Optional
from pyspark.sql import functions as F


class SparkTask:
    def __init__(self, spark_session):
        # Dictionary to store final results
        self.job_counts_dict: Optiona[Dict[str, int]] = None

        # Spark Context and Session
        self.sc = spark_session.sparkContext
        self.spark = spark_session

    def group_sort(self, input_path: str) -> Dict[str, int]:
        df = (
            self.spark.read
            .option("header", True)
            .option("inferSchema", True)
            .csv(input_path)
        )

        df_jobs = (
            df.groupBy("job")
              .agg(F.count("*").alias("count"))
              .orderBy(F.col("count").asc(), F.col("job").asc())
        )

        # NOTE - .collect() moves all data to driver, which maybe inefficient for large data sets
        self.job_counts_dict = { row["job"]: row["count"] for row in df_jobs.collect() }

        return self.job_counts_dict
