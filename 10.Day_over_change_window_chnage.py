from pyspark.sql import functions as F
from pyspark.sql.window import Window

# Step 1: Create a window ordered by order_date.
# This allows us to access the previous day's sales.
w = Window.orderBy("order_date")

# Step 2: Add prev_day_sales using LAG().
# LAG() returns the sales value from the previous row.
# The first row has no previous row, so prev_day_sales will be NULL.
df_result = daily_sales.withColumn(
    "prev_day_sales",
    F.lag("sales").over(w)
)

# Step 3: Calculate the day-over-day (DoD) change.
# DoD change = today's sales - yesterday's sales.
# The first row will also be NULL because prev_day_sales is NULL.
df_result = df_result.withColumn(
    "dod_change",
    F.col("sales") - F.col("prev_day_sales")
)

# Display the result.
df_result.show()
