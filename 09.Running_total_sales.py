from pyspark.sql import functions as F
from pyspark.sql.window import Window

# Step 1: Create a window ordered by order_date.
# This ensures the running total is calculated chronologically.
w = (
    Window
    .orderBy("order_date")
    # Include all previous rows and the current row in the calculation.
    .rowsBetween(
        Window.unboundedPreceding,
        Window.currentRow
    )
)

# Step 2: Calculate the cumulative sum of sales.
# The running_total includes sales from the first row
# up to and including the current row.
# Keep every row — do not use groupBy().
df_result = daily_sales.withColumn(
    "running_total",
    F.sum(F.col("sales")).over(w)
)

# Display the result.
df_result.show()
