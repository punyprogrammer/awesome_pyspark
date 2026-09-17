# sales DataFrame: order_id, customer_id, product_id, amount, order_date
from pyspark.sql import functions as F 
# TODO: customers who placed MORE THAN 5 orders
result = (sales
    .groupBy(
    F.col("customer_id"))
    .agg(
        F.count("*").alias("total_qty")
        )
    .filter(F.col("total_qty") > 5)
    .select("customer_id")
)
result.show()
