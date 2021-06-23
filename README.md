# Open Energy's metadata files for Example Data Provider 

### Metadata files 

Metadata files in `/metadata_files` describe open datasets with real-time energy and CO2 data for BIS headquarters building.

1. **bis-rt-electricity-kwh**
   * contains: data on Electricity kWh
   * source: [Electricity (Energy)](http://search-beta.energydata.org.uk/dataset/real-time-energy-and-co2-data-for-bis-headquarters-building/resource/c13809ba-4b16-4656-9e6b-e1d47b7c6db9)

2. **bis-rt-electricity-co2**
   * contains: data on Electricity kgCO2
   * source: [Electricity (CO2)](http://search-beta.energydata.org.uk/dataset/real-time-energy-and-co2-data-for-bis-headquarters-building/resource/8d69bdae-d58c-4939-b42c-0f8f51989c44)

3. **bis-rt-gas-kwh**
   * contains: data on Gas kWh
   * source: [Gas (Energy)](http://search-beta.energydata.org.uk/dataset/real-time-energy-and-co2-data-for-bis-headquarters-building/resource/2f57766f-1c49-4398-b787-b710b57d7472)


### Data cleanup

The data cleaning process can be reproduced by running `tidy_data.py`, in which the original CSV files are downloaded from source and tidied up following the [Tidy Data Principles](https://vita.had.co.nz/papers/tidy-data.pdf).
The script will aim to save a tidy version of these datasets in `output` folder placed in root directory. 