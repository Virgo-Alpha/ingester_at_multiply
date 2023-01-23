import csv
from client_column_transforms import column_name_mappings
from decimal import Decimal


def is_decimal(data):
    return isinstance(data, Decimal)


def is_int_nullable(data):
    return isinstance(data, (int, type(None)))


def is_string(data):
    # // TODO: Fixme
    return isinstance(data, str)

# Data content validators
def is_positive_number(data):
    return data > 0

# Merchant id is less than 9999
def is_valid_merchant_id(data):
    return data < 9999


column_data_transformers = {
            'merchant_product_id': [str, ],
            'marketplace_product_id': [str, ],
            'name': [str, ],
            'max_price_inc_vat': [Decimal, ],
            # ... other data transformers
            'item_id' : [str, ],
            'min_price_inc_vat': [Decimal, ],
            'stock_qty': [int, ],
            'multiply_merchant_id' : [int, ],
        }

column_data_validators = {
            'merchant_product_id': [is_string, ],
            'marketplace_product_id': [is_string, ],
            'name': [is_string, ],
            'max_price_inc_vat': [is_decimal, is_positive_number, ],
            # ... other validators
            'min_price_inc_vat': [is_decimal, is_positive_number, ],
            'stock_qty': [is_int_nullable, is_positive_number, ],
            'item_id' : [str, ],
            'multiply_merchant_id' : [int, is_valid_merchant_id],
        }

out_rows = []
err_rows = []

with open('data/276_product_update.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        reader.fieldnames = [column_name_mappings.get(
                fieldname, fieldname) for fieldname in reader.fieldnames]
        
        for row in reader:
            # transform data
            print(row)
            
            