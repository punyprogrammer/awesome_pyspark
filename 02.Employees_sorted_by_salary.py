from pyspark.sql.functions import col

# Start with the employees DataFrame
df_result = employees

# Sort employees by salary in descending order
df_result = employees.sort(col("salary").desc())


# ---------------------------------------------------------
# Sorting options in PySpark
# ---------------------------------------------------------

# 1. Sort ascending (default)
# df_result = employees.sort(col("salary").asc())

# 2. Sort descending
# df_result = employees.sort(col("salary").desc())

# 3. orderBy() - equivalent to sort()
# df_result = employees.orderBy(col("salary").desc())

# 4. Sort by multiple columns
# Salary descending, then age ascending
# df_result = employees.orderBy(
#     col("salary").desc(),
#     col("age").asc()
# )

# 5. Using asc() and desc() functions
# from pyspark.sql.functions import asc, desc
#
# df_result = employees.orderBy(
#     desc("salary"),
#     asc("age")
# )

# 6. Sort using column names
# Ascending is the default
# df_result = employees.orderBy("salary")

# 7. Sort using multiple column names
# df_result = employees.orderBy("salary", "age")

# 8. Sort after filtering
# df_result = (
#     employees
#     .filter(col("salary") > 55000)
#     .orderBy(col("salary").desc())
# )

# 9. Sort and get the top N records
# df_result = (
#     employees
#     .orderBy(col("salary").desc())
#     .limit(10)
# )

# Display the sorted DataFrame
df_result.show()
