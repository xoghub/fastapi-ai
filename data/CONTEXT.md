# Context this directory

This is data directory of this project.

This directory not get track by git because data is too big and we don't need to track it.

## Directory Structure
This directory contain 
- [raw](./raw/) data of project in `./raw/` sub-directory
- [references](./references/) paper of references in `./references/` sub-directory
- [clean](./clean/) data that raw data preprocessing from [Preprocessing Code](./) this directory in `./clean/` sub-directory
- [scrape](./scrape/) is director for script to scrape data from web that will add in [raw](./raw/) sub-directory, but don't remove previous data and always create new file with new name for each scrape
- `scrape.py` is main file to run scrape script, will give a output `raw/scraped-data.csv`

Even though this data sub-directory is in `.gitignore` but you still need to create new file and inside this directory to add version of data that use in models. for keep it easy to track which data that use for model training. or using comment inside code of data name, or something clear to understand which data that use for model training.

## Naming Conventions
Good naming convention example :
- `raw/scraped-data_YYYY-MM-DD.csv` for raw data
- `clean/scraped-data_YYYY-MM-DD_cleaned_YYYY-MM-DD.csv` for cleaned data
- `scrape/scraped-[platform].py` for [platform] is name of platform e.g. Tokopedia, Shopee, TikTok, etc for scraping code
- `references/[title-of-paper].pdf` for [name] is name of paper e.g. aspect-based-sentiment-analysis for paper reference

where YYYY-MM-DD is the date when the data was created

## Routing
| Task | Go to | Read |
|------|-------|------|
| Scrape Data | ./scrape | CONTEXT.md |
| Store Clean Data | ./clean | CONTEXT.md |
| Store Raw Data | ./raw | CONTEXT.md |
| Review and Research about [model] based on Reference Paper [name_of_paper] | ./references | CONTEXT.md |
