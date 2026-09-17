# sales DataFrame: order_id, customer_id, product_id, amount, order_date
# F = pyspark.sql.functions
# spark and sales DataFrames are already available.

# Step 1: Group the sales by customer_id.
# Step 2: Calculate the total sales for each customer.
# Step 3: Sort customers by total_sales in descending order.
# Step 4: Keep only the top 3 customers.
result = (
    sales
    .groupBy("customer_id")
    .agg(
        F.sum("amount").alias("total_sales")
    )
    .orderBy(
        F.col("total_sales").desc()
    )
    .limit(3)
)

# Display the result.
result.show()
