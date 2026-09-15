from pyspark.sql import functions as F

df_result = employees  # TODO: Group employees by city, count employees, and order by count


# COUNT
# Count the number of employees in each city.
df_result = (
    df_result
    .groupBy(F.col("city"))
    .agg(
        F.count("*").alias("count")
    )
    .orderBy(F.col("count"))
)


# ---------------------------------------------------------
# OTHER COMMON AGGREGATION METHODS
# ---------------------------------------------------------

# COUNT DISTINCT
# Count the number of unique employees/customers in each city.
# Useful when the DataFrame may contain duplicate employee records.
df_result = (
    employees
    .groupBy("city")
    .agg(
        F.countDistinct("employee_id").alias("unique_employees")
    )
)


# SUM
# Calculate the total salary for each city.
df_result = (
    employees
    .groupBy("city")
    .agg(
        F.sum("salary").alias("total_salary")
    )
)


# AVG
# Calculate the average salary for each city.
df_result = (
    employees
    .groupBy("city")
    .agg(
        F.avg("salary").alias("average_salary")
    )
)


# MIN
# Find the minimum salary in each city.
df_result = (
    employees
    .groupBy("city")
    .agg(
        F.min("salary").alias("minimum_salary")
    )
)


# MAX
# Find the maximum salary in each city.
df_result = (
    employees
    .groupBy("city")
    .agg(
        F.max("salary").alias("maximum_salary")
    )
)


# MULTIPLE AGGREGATIONS
# Calculate multiple statistics for each city in a single aggregation.
df_result = (
    employees
    .groupBy("city")
    .agg(
        F.count("*").alias("employee_count"),
        F.sum("salary").alias("total_salary"),
        F.avg("salary").alias("average_salary"),
        F.min("salary").alias("minimum_salary"),
        F.max("salary").alias("maximum_salary")
    )
)


# CONDITIONAL AGGREGATION
# Count only employees whose salary is greater than 100000.
# when() creates a condition and count() counts the non-null results.
df_result = (
    employees
    .groupBy("city")
    .agg(
        F.count(
            F.when(F.col("salary") > 100000, 1)
        ).alias("high_salary_employees")
    )
)


# CONDITIONAL SUM
# Calculate the total salary of employees earning more than 100000.
df_result = (
    employees
    .groupBy("city")
    .agg(
        F.sum(
            F.when(F.col("salary") > 100000, F.col("salary"))
             .otherwise(0)
        ).alias("high_salary_total")
    )
)


# COLLECT_LIST
# Collect all employee names for each city.
# Duplicates are preserved.
df_result = (
    employees
    .groupBy("city")
    .agg(
        F.collect_list("name").alias("employees")
    )
)


# COLLECT_SET
# Collect unique employee names for each city.
# Duplicate values are removed.
df_result = (
    employees
    .groupBy("city")
    .agg(
        F.collect_set("name").alias("unique_employees")
    )
)


# AGGREGATION WITHOUT GROUPING
# Calculate statistics for the entire DataFrame instead of per city.
df_result = employees.agg(
    F.count("*").alias("total_employees"),
    F.sum("salary").alias("total_salary"),
    F.avg("salary").alias("average_salary"),
    F.min("salary").alias("minimum_salary"),
    F.max("salary").alias("maximum_salary")
)


# ORDER BY AGGREGATED COLUMN
# First calculate the employee count for each city,
# then sort the result by employee count in ascending order.
df_result = (
    employees
    .groupBy("city")
    .agg(
        F.count("*").alias("employee_count")
    )
    .orderBy(F.col("employee_count"))
)


# ORDER BY DESCENDING
# Sort cities from highest employee count to lowest.
df_result = (
    employees
    .groupBy("city")
    .agg(
        F.count("*").alias("employee_count")
    )
    .orderBy(F.col("employee_count").desc())
)


# GROUP BY MULTIPLE COLUMNS
# Calculate the number of employees for each city and department combination.
df_result = (
    employees
    .groupBy("city", "department")
    .agg(
        F.count("*").alias("employee_count")
    )
)


# FILTER BEFORE AGGREGATION
# Filter employees first, then calculate the average salary for each city.
df_result = (
    employees
    .filter(F.col("salary") > 50000)
    .groupBy("city")
    .agg(
        F.avg("salary").alias("average_salary")
    )
)


# HAVING-LIKE FILTER AFTER AGGREGATION
# Keep only cities having more than 10 employees.
# filter() is applied after agg(), similar to SQL HAVING.
df_result = (
    employees
    .groupBy("city")
    .agg(
        F.count("*").alias("employee_count")
    )
    .filter(F.col("employee_count") > 10)
)


# DISPLAY THE FINAL RESULT
df_result.show()
