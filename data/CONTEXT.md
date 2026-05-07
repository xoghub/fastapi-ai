# Context this directory

This is data directory of this project.

This directory not get track by git because data is too big and we don't need to track it.

This directory contain 
- [raw](./raw/) data of project in `./raw/` sub-directory
- [references](./references/) paper of references in `./references/` sub-directory
- [clean](./clean/) data that raw data preprocessing from [Preprocessing Code](./) this directory in `./clean/` sub-directory
- [scrape](./scrape/) is director for script to scrape data from web that will add in [raw](./raw/) sub-directory, but don't remove previous data and always create new file with new name for each scrape
- `scrape.py` is main file to run scrape script, will give a output `raw/scraped-data.csv`

Even though this data sub-directory is in `.gitignore` but you still need to create new file and inside this directory to add version of data that use in models. for keep it easy to track which data that use for model training. or using comment inside code of data name, or something clear to understand which data that use for model training.

Good naming convention example :
- `raw/scraped-data-YYYY-MM-DD.csv` for raw data
- `clean/scraped-data_YYYY-MM-DD_cleaned_YYYY-MM-DD.csv` for cleaned data

where YYYY-MM-DD is the date when the data was created
