# sales_data DataFrame: order_id, product, region, quantity
# F is already imported from pyspark.sql.functions.

result = (sales_data
         .groupBy(F.col('product'))
         .agg(
            F.sum("quantity").alias('total_qty'),
            F.sum(
                F.when(F.col("region")=="West",F.col("quantity"))
                .otherwise(0)
            ).alias("west_qty"),
            F.countDistinct("region").alias("region_count"),
            F.count("*").alias("order_count")
            )
            .orderBy(F.col("product"))
)

result.show()
