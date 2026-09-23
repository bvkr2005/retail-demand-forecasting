# Databricks notebook source
calendar_path = "/Volumes/workspace/default/m5_raw/calendar.csv"

calendar_df = spark.read.option("header", True).option("inferSchema", True).csv(calendar_path)

display(calendar_df.limit(10))

# COMMAND ----------

row_count = calendar_df.count()
column_count = len(calendar_df.columns)

print("Number of rows:", row_count)
print("Number of columns:", column_count)

# COMMAND ----------

calendar_df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Missing Values
# MAGIC
# MAGIC Check each calendar column for null values to understand where data may be incomplete.

# COMMAND ----------

from pyspark.sql.functions import col, sum as spark_sum

null_counts = calendar_df.select([
    spark_sum(col(c).isNull().cast("int")).alias(c)
    for c in calendar_df.columns
])

display(null_counts)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Date Range
# MAGIC
# MAGIC Identify the earliest and latest dates available in the calendar dataset.

# COMMAND ----------

from pyspark.sql.functions import min, max

calendar_df.select(
    min("date").alias("start_date"),
    max("date").alias("end_date")
).show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Cardinality
# MAGIC
# MAGIC Check the number of unique values in key calendar fields.

# COMMAND ----------

from pyspark.sql.functions import countDistinct

calendar_df.select(
    countDistinct("date").alias("unique_dates"),
    countDistinct("wm_yr_wk").alias("unique_weeks"),
    countDistinct("weekday").alias("unique_weekdays"),
    countDistinct("year").alias("unique_years"),
    countDistinct("event_name_1").alias("unique_primary_events"),
    countDistinct("event_type_1").alias("unique_primary_event_types")
).show()

# COMMAND ----------

calendar_df.select("year").distinct().orderBy("year").show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Event Types and SNAP Indicators
# MAGIC
# MAGIC Inspect the event categories and SNAP indicator values available in the calendar dataset.

# COMMAND ----------

calendar_df.select("event_type_1") \
    .distinct() \
    .orderBy("event_type_1") \
    .show()

# COMMAND ----------

calendar_df.select(
    "snap_CA",
    "snap_TX",
    "snap_WI"
).distinct().show()

# COMMAND ----------

# MAGIC %md
# MAGIC # Sales Data Profiling
# MAGIC
# MAGIC This section profiles the M5 historical daily sales dataset.

# COMMAND ----------

sales_path = "/Volumes/workspace/default/m5_raw/sales_train_validation.csv"

sales_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(sales_path)
)

display(sales_df.limit(5))

# COMMAND ----------

sales_row_count = sales_df.count()
sales_column_count = len(sales_df.columns)

print("Number of rows:", sales_row_count)
print("Number of columns:", sales_column_count)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Column Structure
# MAGIC
# MAGIC The sales dataset contains identifier columns followed by daily sales columns in wide format.

# COMMAND ----------

id_columns = [
    "id",
    "item_id",
    "dept_id",
    "cat_id",
    "store_id",
    "state_id"
]

day_columns = [c for c in sales_df.columns if c.startswith("d_")]

print("Identifier columns:", len(id_columns))
print("Daily sales columns:", len(day_columns))
print("First daily column:", day_columns[0])
print("Last daily column:", day_columns[-1])

# COMMAND ----------

# MAGIC %md
# MAGIC ## Sales Cardinality
# MAGIC
# MAGIC Count the unique items, departments, categories, stores, and states represented in the sales dataset.

# COMMAND ----------

from pyspark.sql.functions import countDistinct

sales_df.select(
    countDistinct("item_id").alias("unique_items"),
    countDistinct("dept_id").alias("unique_departments"),
    countDistinct("cat_id").alias("unique_categories"),
    countDistinct("store_id").alias("unique_stores"),
    countDistinct("state_id").alias("unique_states")
).show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Product and Store Hierarchy
# MAGIC
# MAGIC Inspect the categories, departments, stores, and states represented in the sales dataset.

# COMMAND ----------

print("Categories:")
sales_df.select("cat_id").distinct().orderBy("cat_id").show()

print("Departments:")
sales_df.select("dept_id").distinct().orderBy("dept_id").show()

print("Stores:")
sales_df.select("store_id").distinct().orderBy("store_id").show()

print("States:")
sales_df.select("state_id").distinct().orderBy("state_id").show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Missing Values
# MAGIC
# MAGIC Check the sales dataset for missing values across identifier and daily sales columns.

# COMMAND ----------

from pyspark.sql.functions import col, sum as spark_sum

null_counts = sales_df.select([
    spark_sum(col(c).isNull().cast("int")).alias(c)
    for c in sales_df.columns
]).collect()[0].asDict()

columns_with_nulls = {
    column: count
    for column, count in null_counts.items()
    if count > 0
}

print("Columns with null values:", len(columns_with_nulls))
print(columns_with_nulls)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Sales Date Range
# MAGIC
# MAGIC Map the first and last daily sales columns to the calendar dataset to determine the historical sales period.

# COMMAND ----------

sales_day_range = calendar_df.filter(
    col("d").isin(day_columns[0], day_columns[-1])
).select(
    "d",
    "date"
).orderBy("date")

sales_day_range.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Sales Value Range
# MAGIC
# MAGIC Check the minimum and maximum unit sales values across the daily sales columns.

# COMMAND ----------

from pyspark.sql.functions import array_min, array_max, array, col, min as spark_min, max as spark_max

sales_values = sales_df.select(
    array_min(array(*[col(c) for c in day_columns])).alias("row_min"),
    array_max(array(*[col(c) for c in day_columns])).alias("row_max")
)

sales_values.select(
    spark_min("row_min").alias("minimum_sales"),
    spark_max("row_max").alias("maximum_sales")
).show()

# COMMAND ----------

# MAGIC %md
# MAGIC # Sell Prices Data Profiling
# MAGIC
# MAGIC This section profiles the M5 product selling price dataset.

# COMMAND ----------

prices_path = "/Volumes/workspace/default/m5_raw/sell_prices.csv"

prices_df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(prices_path)
)

display(prices_df.limit(10))

# COMMAND ----------

prices_row_count = prices_df.count()
prices_column_count = len(prices_df.columns)

print("Number of rows:", prices_row_count)
print("Number of columns:", prices_column_count)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Missing Values
# MAGIC
# MAGIC Check the sell prices dataset for missing values.

# COMMAND ----------

from pyspark.sql.functions import col, sum as spark_sum

prices_df.select([
    spark_sum(col(c).isNull().cast("int")).alias(c)
    for c in prices_df.columns
]).show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Sell Prices Cardinality
# MAGIC
# MAGIC Count the unique stores, items, and weeks represented in the sell prices dataset.

# COMMAND ----------

from pyspark.sql.functions import countDistinct

prices_df.select(
    countDistinct("store_id").alias("unique_stores"),
    countDistinct("item_id").alias("unique_items"),
    countDistinct("wm_yr_wk").alias("unique_weeks")
).show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Sell Price Range
# MAGIC
# MAGIC Check the minimum and maximum selling prices in the dataset.

# COMMAND ----------

from pyspark.sql.functions import min as spark_min, max as spark_max

prices_df.select(
    spark_min("sell_price").alias("minimum_price"),
    spark_max("sell_price").alias("maximum_price")
).show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Sell Prices Date Range
# MAGIC
# MAGIC Use the M5 calendar to determine the date range covered by the sell prices dataset.

# COMMAND ----------

price_weeks = prices_df.select("wm_yr_wk").distinct()

price_date_range = (
    price_weeks
    .join(
        calendar_df.select("wm_yr_wk", "date"),
        on="wm_yr_wk",
        how="inner"
    )
)

price_date_range.select(
    spark_min("date").alias("start_date"),
    spark_max("date").alias("end_date")
).show()

# COMMAND ----------

prices_df.printSchema()