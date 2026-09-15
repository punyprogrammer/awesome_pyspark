from pyspark.sql.functions import col

# Start with the employees DataFrame
df_result = employees

# ---------------------------------------------------------
# Filtering options in PySpark
# ---------------------------------------------------------

# 1. Basic comparison
# Filter employees with salary greater than 55,000
df_result = df_result.filter(col("salary") > 55000)


# 2. Equality
# df_result = df_result.filter(col("department") == "Engineering")


# 3. Not equal
# df_result = df_result.filter(col("department") != "HR")


# 4. Multiple conditions - AND
# Use & instead of Python's "and"
# Parentheses are required around each condition
# df_result = df_result.filter(
#     (col("salary") > 55000) &
#     (col("department") == "Engineering")
# )


# 5. Multiple conditions - OR
# Use | instead of Python's "or"
# df_result = df_result.filter(
#     (col("department") == "Engineering") |
#     (col("department") == "Data")
# )


# 6. Filter using IN
# Keep employees belonging to any of these departments
# df_result = df_result.filter(
#     col("department").isin("Engineering", "Data", "Analytics")
# )


# 7. Filter NULL values
# df_result = df_result.filter(col("email").isNull())


# 8. Filter NOT NULL values
# df_result = df_result.filter(col("email").isNotNull())


# 9. String contains
# df_result = df_result.filter(
#     col("email").contains("@gmail.com")
# )


# 10. String starts with
# df_result = df_result.filter(
#     col("name").startswith("A")
# )


# 11. Filter using a SQL expression
# df_result = df_result.filter(
#     "salary > 55000 AND department = 'Engineering'"
# )


# 12. where() is an alias for filter()
# df_result = df_result.where(col("salary") > 55000)


# Display the filtered DataFrame
df_result.show()
