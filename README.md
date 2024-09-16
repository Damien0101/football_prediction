#  Football Prediction ⚽🏆


![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white)

## 📜 Project Description
#### The football match prediction project aims to predict results of Belgian Jupiler Pro League games using scraping, machine learning, and data visualization. Using SQL for data management, Airflow to automate data updates, and Streamlit for live visualizations, this project predicts match results, displays betting odds, and shows team stats. This helps football analysts and fans make informed predictions. ####

[![N|Solid](utils/images/football.png "vivino")](https://footballpredict.streamlit.app/)

***click on the image to make your first prediction...***

## 👀 Project Overview 

- #### scraper : Includes Python scripts for web scraping to collect recent match data and betting odds from football websites, updated regularly using Airflow.

- #### database : Stores both historical and scraped data in a structured format, managed through SQL, for easy querying and analysis. 

- #### preprocess : Contains scripts for cleaning and preparing raw data for analysis and model training, ensuring consistency and accuracy.

- #### model : Houses machine learning scripts that train prediction models on historical data and periodically retrain them with updated information. 

- #### app.py: The main application script for deploying a Streamlit web interface, allowing users to explore match predictions, team stats, and visualizations.



## 🤖 Sample Code 
```python
# instantiate the cloudscraper object
scraper = cloudscraper.create_scraper()

def fetch_and_parse_html(url: str) -> bs:
    """ Fetches and parses the HTML content of the webpage. """ 
    response = scraper.get(url)
    return bs(response.content, 'html.parser')
```

## ⏱️ Project Timeline 

### 1. Project Setup and Data Exploration

Set up the environment, repository, and explore the provided match data to understand its structure and key features.

### 2. Data Scraping

Develop web scrapers to collect real-time match data and betting odds from football websites.

### 3. Data Preprocessing

Clean and preprocess the raw and scraped data, ensuring it is ready for model training and analysis.

### 4. Model Training

Train machine learning models on historical match data to predict outcomes, and evaluate model performance.

### 5. Streamlit App Development

Build a Streamlit app to display live match predictions, team stats, and betting odds, allowing users to see the predictions

### 6. Airflow Automation Setup

Integrate Airflow to automate data scraping, preprocessing, and periodic model retraining..

## ⛓️ Project Directory Structure 

```plaintext
FOOTBALL_PREDICTION_PROJECT
│
├── data
├── pages
├── query
│
├── utils
│   ├── database
│   ├── images
│   ├── model
│   ├── preprocess
│   ├── scraper
│   └── visual
│
├── diagram_db.drawio
├── README.md
└── requirements.txt

```
   

## 🔧  Installation

### To run the app locally, follow these steps :

1. #### Clone the repository :

    
    ```sh
    git clone https://github.com/servietsky0/football_prediction
    ```
    

2. #### Navigate into the cloned repository :

    
    ```sh
    cd football_prediction/ 
    ```


3. #### Install the necessary dependencies using pip :

    
    ```sh
    pip install -r requirements.txt
    ```
    

4. #### Once you did all the these steps, type this commande in the terminal :

   ```sh
   streamlit run JPL_Football_Predictions.py
   ```
      
    #### Or visit :
    [Football Prediction app](https://footballpredict.streamlit.app/) 

## 🫂 Collaborators 
[Ben Ozfirat](https://github.com/benozfirat) - Data Analyst

[Volodymyr Vysotski](https://github.com/vvvladimir65) - Data Analyst

[Ness Gira](https://github.com/ness015618) - Data Engineer

[Damien Compere](https://github.com/servietsky0) - Data Engineer

## 🎉 Have Fun!

#### *I hope you enjoy using my football prediction app as much as I enjoyed building it! Each prediction and stat brings us one step closer to understanding the game more deeply.* 🚀