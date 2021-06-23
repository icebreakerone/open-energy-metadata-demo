import pandas as pd
import numpy as np

url1 = 'https://savenergyonline.stark.co.uk/government/BIS/Reports/DYTS01_kWh.csv'
url2 = 'https://savenergyonline.stark.co.uk/government/BIS/Reports/DYTS01_CO2.csv'
url3 = 'https://savenergyonline.stark.co.uk/government/BIS/Reports/DYTS02_kWh.csv'

def tidy_data(url, skiprows, value_name, output_name):

    # download data
    raw_data = pd.read_csv(url, error_bad_lines=False, skiprows=skiprows)

    # transform wide to long format
    tidy_data = raw_data.melt(id_vars=["Site Name", "Utility", "Type", "Date"],
                            var_name="Time",
                            value_name=value_name)

    # tidy up colnames
    tidy_data.columns = map(str.lower, tidy_data.columns)
    tidy_data.columns = tidy_data.columns.str.replace(' ', '_')

    # unify missing values
    tidy_data = tidy_data.replace(['N/A', '', ' ', '-'], np.NaN)

    # save tidy dataset in ./output folder
    tidy_data.to_csv(f"output/{output_name}", index=False)

### Tidy up datasets
tidy_data(url1, skiprows=3, value_name="Electricity kWh", output_name="tidy_DYTS01_kWh.csv")
tidy_data(url2, skiprows=4, value_name="Electricity kgCO2", output_name="tidy_DYTS01_CO2.csv")
tidy_data(url3, skiprows=3, value_name="Gas kWh", output_name="tidy_DYTS02_kWh.csv")
