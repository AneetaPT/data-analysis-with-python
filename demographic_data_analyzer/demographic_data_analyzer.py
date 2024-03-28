import pandas as pd


def calculate_demographic_data():
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men =round( df[df['sex']=='Male']['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    n= len(df[df['education']=="Bachelors"])
    t=len(df)
    percentage_bachelors =round((n/t)*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors','Masters','Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors','Masters','Doctorate'])]

    # percentage with salary >50K
    advanced_education_high_income=(higher_education[higher_education['salary']=='>50K'])
    higher_education_rich = round(len(advanced_education_high_income)/len(higher_education)*100,1)
    l=len(lower_education[lower_education['salary']=='>50K'])
    lower_education_rich = round(l/len(lower_education)*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours =df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    m=df[df['hours-per-week']==min_work_hours]
    s=m[m['salary']=='>50K']

    rich_percentage = round((len(s)/len(m))*100,1)

    # What country has the highest percentage of people that earn >50K?
    high_income = df[df['salary'] == '>50K']
    percentage_high_earning = (high_income['native-country'].value_counts() / df['native-country'].value_counts()) * 100
    highest_earning_country =percentage_high_earning.idxmax()
    highest_earning_country_percentage = round(percentage_high_earning.max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    indian_high_income =high_income[high_income['native-country']=='India']
    top_IN_occupation = indian_high_income ['occupation'].value_counts().idxmax()
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
calculate_demographic_data