from pyspark.sql.functions import sum, avg, col


# TODO: Group by customer_id and calculate total_sales and avg_order_value

df_result = orders

df_result = (
    df_result
    .groupBy("customer_id")
    .agg(
        sum(col("order_value")).alias("total_sales"),
        avg(col("order_value")).alias("avg_order_value")
    )
)

df_result.show()
