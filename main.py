# Specific instructions
# 0. This code is written and tested in Python >= 3.6
# 1. Do not use any libraries that are not part of the python stndard lib
# 2. What is given here is a guide, while it is meant to be useful, 
# you are free to modify any part of it as you wish

import csv
import os

from client_column_transforms import column_name_mappings
from ingest import MerchantDataFileHandler
merchant_data_file_name = '276_product_update.csv'
merchant_data_file_path = os.path.join('.', 'data', merchant_data_file_name)
output_file = 'db_ready_output.csv'

# I replaced the hard coded merchant number with a dynamic one based on the 
# file name
merchant_number = int(merchant_data_file_name.split('_')[0])

if __name__ == '__main__':
    mdfh = MerchantDataFileHandler(merchant_number, merchant_data_file_path, 
    column_name_mappings[merchant_number])
    out_rows, out_err = mdfh.generate_output_file_contents()
    if out_rows:
        with open(output_file, 'w') as dbfile:
            fieldnames = out_rows[0].keys()
            writer = csv.DictWriter(dbfile, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(out_rows)

            # To separate the error log from the output file, I rewrite the 
            # headers again
            if out_err:
                writer.writeheader()
                writer.writerows(out_err)


# ? err_rows as an error log section of the file with a reason why/@ least an
#  indication of the error
# ! Check log file examples for inspiration
