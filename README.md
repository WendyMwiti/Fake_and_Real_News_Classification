# **Fake And Real News Classification**

![image](https://user-images.githubusercontent.com/60213013/204645379-7197e7c4-b106-4359-b0e4-f84ad1221f00.png)


### Authors: [Femi Kamau](https://www.github.com/ctrl-Karugu), [Monicah Iwagit](https://github.com/Okodoimonicah), [Teofilo Gafna](https://github.com/teofizzy)


---

> This project is a part of the [Data Science (DSF-FT)](https://moringaschool.com/courses/data-science-course/) Course at [Moringa School](https://moringaschool.com/). The full project description can be found [here](https://github.com/learn-co-curriculum/dsc-phase-4-project-v2-3).

# Table of Contents: 
* Overview
* Business Problem
* Data Understanding - The dataset was sourced from [Kaggle](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
* Data Cleaning: Validity, Completeness, Consistency, Uniformity
* Exploratory Data Analysis
* Modeling:
    * Preprocessing techniques in NLP
    * Building models
    * Model validation
 * Deployment
    
    
# Project Description:
With the current technology, almost every individual has an access to internet and there are no restrictions to what one posts. 
With this, people can obtain news from them and believe that they are legitimate which might not be case.
Feeding information from the internet can affect oneself in one way or another.
To avoid this, this project aims to analyse data using text classification with NLP to determine whether an article posted is real or not.
    

# Technologies Used:
   * Pandas
   * Seaborn
   * Scikit-Learn
   * NLTK
   * Streamlit
    

# Project Features:
From the data set, the project focuses on the text column as the independent and category column as the dependent variable.
    

# Project Future Use:
Using this project one will be able to tell whether or not an article is legitimate which will improve on how people percieve on things and situations.



# Deployment:
The project was deployed using [Streamlit](https://streamlit.io/). The link to the deployed project can be found [here](https://beast001-fake-and-real-news-classification-demoml-app-tbg7es.streamlit.app/)

# Repository Structure:

```
    ├── README.md
    | 
    ├── .gitignore
    | 
    |── index.ipynb    
    | 
    ├── models
    |    └── model.pkl
    | 
    ├── demo
    |    ├── requirements.txt
    |    └── ml-app.py
    |
    └── data_preprocessing
         ├── cities.txt
         ├── countries.txt
         ├── months.txt
         ├── names.txt
         ├── states.txt
         └── week.txt

```
