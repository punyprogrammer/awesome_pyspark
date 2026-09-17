from pyspark.sql import functions as F
from pyspark.sql.window import Window

# Step 1: Create a window ordered by value.
# This allows us to access the previous value for each row.
w = Window.orderBy("value")

# Step 2: Add the previous value to each row using LAG().
df_result = numbers.withColumn(
    "prev_value",
    F.lag("value").over(w)
)

# Step 3: Calculate the difference between the current value
# and the previous value, then find the maximum difference.
df_result = df_result.select(
    F.max(
        F.col("value") - F.col("prev_value")
    ).alias("max_diff")
)

# Display the result.
df_result.show()
