# orders and customers are assumed to be existing PySpark DataFrames.

df_result = orders  # TODO: Join with customers on customer_id


# INNER JOIN
# Returns only rows where customer_id exists in both DataFrames.
df_result = df_result.join(
    customers,
    "customer_id",
    "inner"
)


# LEFT JOIN / LEFT OUTER JOIN
# Returns all rows from orders and matching rows from customers.
# Non-matching customer records will have NULL values.
df_result = orders.join(
    customers,
    "customer_id",
    "left"
)


# RIGHT JOIN / RIGHT OUTER JOIN
# Returns all rows from customers and matching rows from orders.
# Non-matching order records will have NULL values.
df_result = orders.join(
    customers,
    "customer_id",
    "right"
)


# FULL JOIN / FULL OUTER JOIN
# Returns all rows from both DataFrames.
# Non-matching rows will have NULL values on the other side.
df_result = orders.join(
    customers,
    "customer_id",
    "full"
)


# LEFT SEMI JOIN
# Returns only rows from orders that have a matching customer.
# Unlike INNER JOIN, columns from customers are NOT included.
df_result = orders.join(
    customers,
    "customer_id",
    "left_semi"
)


# LEFT ANTI JOIN
# Returns only rows from orders that do NOT have a matching customer.
# Useful for finding unmatched/orphan records.
df_result = orders.join(
    customers,
    "customer_id",
    "left_anti"
)


# CROSS JOIN
# Produces every possible combination of rows from both DataFrames.
# Be careful: the resulting number of rows can become very large.
df_result = orders.crossJoin(customers)


# USING COLUMN NAME
# When both DataFrames have the same join-column name,
# the column name can be passed directly as a string.
df_result = orders.join(
    customers,
    "customer_id"
)


# MULTIPLE JOIN COLUMNS
# Use a list when the join requires multiple columns.
df_result = orders.join(
    customers,
    ["customer_id", "city"],
    "inner"
)


# JOIN USING A CONDITION
# Use this approach when the join condition is more complex
# than simply matching columns with the same name.
from pyspark.sql.functions import col

df_result = orders.alias("o").join(
    customers.alias("c"),
    col("o.customer_id") == col("c.customer_id"),
    "inner"
)


# DISPLAY THE FINAL RESULT
df_result.show()
