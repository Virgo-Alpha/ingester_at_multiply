import csv
from decimal import Decimal
from client_column_transforms import column_name_mappings

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
        }
        
    def generate_output_file_contents(self):
        # 1. read input file
        # 2. validate data
        # 3. create output contents (inject multiply merchant id here)
        out_rows = []
        err_rows = []

        # TODO: Implement me
        with open(self.file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            reader.fieldnames = [self.column_name_mapping.get(field, field) for field in reader.fieldnames]
            
            # 1. read input file
            for row in reader:

                for key, value in row.items():
                    for transformer in self.column_data_transformers[key]:
                        value = transformer(value)
                        row[key] = value
            
        return  out_rows, err_rows
