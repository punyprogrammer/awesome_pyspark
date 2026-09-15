from pyspark.sql.functions import col

# employees has columns: name, city, salary

# =========================================================
# 1. select() with column names
# =========================================================
df_result = employees.select("name", "city")


# =========================================================
# 2. select() with col()
# =========================================================
df_result = employees.select(
    col("name"),
    col("city")
)


# =========================================================
# 3. selectExpr()
# =========================================================
df_result = employees.selectExpr("name", "city")


# =========================================================
# 4. Using DataFrame column attributes
# =========================================================
df_result = employees.select(
    employees.name,
    employees.city
)


# =========================================================
# 5. Using DataFrame column indexing
# =========================================================
df_result = employees.select(
    employees["name"],
    employees["city"]
)


# =========================================================
# 6. Using a list with unpacking
# =========================================================
columns_to_keep = ["name", "city"]
df_result = employees.select(*columns_to_keep)


# =========================================================
# 7. Using drop() when only one column needs removing
# =========================================================
# Since employees has only name, city, and salary,
# dropping salary leaves only name and city.
df_result = employees.drop("salary")


# =========================================================
# 8. selectExpr() with aliases
# =========================================================
# Useful when you also want to rename columns or apply expressions.
df_result = employees.selectExpr(
    "name AS employee_name",
    "city AS employee_city"
)


# =========================================================
# 9. Selecting columns with aliases using col()
# =========================================================
df_result = employees.select(
    col("name").alias("employee_name"),
    col("city").alias("employee_city")
)


# =========================================================
# Display the result
# =========================================================
df_result.show()
