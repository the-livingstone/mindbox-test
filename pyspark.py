from pyspark.sql import DataFrame

def get_product_categories(prod_df: DataFrame, cat_df: DataFrame) -> DataFrame:
    return prod_df.join(cat_df,  prod_df.id == cat_df.id,  'leftouter').select(prod_df.id, cat_df.id)