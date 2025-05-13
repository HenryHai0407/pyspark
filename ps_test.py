import pandas as pd
import numpy as np
from pyspark.sql import SparkSession
import pyspark
# Get the version of PySpark
pyspark_version = pyspark.__version__
print(f"PySpark Version: {pyspark_version}")