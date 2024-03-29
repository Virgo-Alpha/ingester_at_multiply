import csv
from decimal import Decimal
from client_column_transforms import column_name_mappings
# from types import NoneType

# Data type validators
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

# Read column names (header)
class MerchantDataFileHandler:

    def __init__(self, multiply_merchant_id, file_path, column_name_mapping):
        self.multiply_merchant_id = multiply_merchant_id
        self.file_path = file_path
        self.column_name_mapping = column_name_mapping

        # // TODO: Add more column validators and
        # // data transformers as appropriate
        self.column_data_validators = {
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

        self.column_data_transformers = {
            'merchant_product_id': [str, ],
            'marketplace_product_id': [str, ],
            'name': [str, ],
            'max_price_inc_vat': [Decimal, ],
            # ... other data transformers
            'min_price_inc_vat': [Decimal, ],
            'stock_qty': [int, ],
            'multiply_merchant_id' : [int, ],
            'item_id' : [str, ],
        }

    def generate_output_file_contents(self):
        # // 1. read input file
        # // 2. validate data
        # 3. create output contents (inject multiply merchant id here)
        out_rows = []
        err_rows = []

        # TODO: Implement me

        with open(self.file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            # map fieldnames using column_name_mappings
            reader.fieldnames = [self.column_name_mapping.get(
                fieldname, fieldname) for fieldname in reader.fieldnames]
            
            for row in reader:

                for key, value in row.items():
                    try:
                        # transform data
                        # // ! rename value to transformed_value
                        # // ! loop over the transformers
                        for transformer in self.column_data_transformers[key]:
                            transformed_value = transformer(value)
                            value = transformed_value

                        # transformed_value = self.column_data_transformers[key][0](value)
                        # value = transformed_value
                    except Exception as e:
                        # // ! I think you meant to break here,
                        # // ! otherwise only one transformer will be applied
                        break
                
                # validate data
                try:
                    for validator in self.column_data_validators[key]:
                        if not validator(value):
                            err_rows.append(row)
                            break
                        else:
                            out_rows.append(row)
                            break
                except Exception as e:
                            break
                    
        return out_rows, err_rows
