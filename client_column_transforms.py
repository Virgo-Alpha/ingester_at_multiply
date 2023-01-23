"""
This file contains the column name mappings for each client.
This is important because the column names in the merchant data files are not 
consistent and differ from those in multiply's database."""

column_name_mappings ={ 
    # multiply_merchant_id: {transform_mapping},
    421: {
        "prod_id": "merchant_product_id",
        # // You will need to create the rest of this
        "mktplc_prod_id" : "marketplace_product_id",
        "max_selling_price" : "max_price_inc_vat",
        "min_selling_price" : "min_price_inc_vat",
        "inventory_level" : "stock_qty",
         },
    276 : {
        "item_id": "merchant_product_id",
        "mkt_plc_prod_id": "marketplace_product_id",
        "highest_price": "max_price_inc_vat",
    },
    # other client column name mappings can go here if needed
}