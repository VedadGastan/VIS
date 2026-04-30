# Used Car Market Analysis — Bosnia & Herzegovina

Analysis of the used car market in BiH using data scraped from [olx.ba](https://olx.ba/), one of the most popular car listing platforms in the region.

## Project Structure

This project is split into two repositories:

- **[VIS-Zadaca-2](https://github.com/VedadGastan/VIS-Zadaca-2)** — Web scraper that collects car listings from olx.ba and saves them to CSV
- **[VIS](https://github.com/VedadGastan/VIS)** — Data analysis notebook (this repo)

## Data Collection

The scraper uses Selenium and BeautifulSoup to extract listing details including manufacturer, model, fuel type, year, transmission, mileage, engine displacement, power, and price. Duplicate links are filtered out and data is cleaned before analysis.

## Analysis

The notebook (`VIS24_Z2_TIM41.ipynb`) covers:

- Data cleaning and preprocessing
- Descriptive statistics and visualisation of all columns
- Chi-square tests for categorical variable independence
- Confidence interval estimation for proportions and numerical variables
- Normality testing
- Hypothesis testing
- Linear regression for price prediction (R² = 0.722)

## Tech Stack

- Python
- Selenium & BeautifulSoup (scraping)
- Pandas (data manipulation)
- Matplotlib, Seaborn, Plotly (visualisation)
- SciPy (statistical testing)

## Results

The linear regression model explains 72.2% of price variability. Engine power, displacement, and year of manufacture are the strongest positive predictors of car price.

## Team

Vedad, Nejira, Maida, Elvedina
