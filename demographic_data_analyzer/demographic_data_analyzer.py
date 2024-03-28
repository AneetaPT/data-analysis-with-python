{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1802fb2a-3a49-4919-85ad-9985a82119ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "4c200cee-579c-4bc4-b251-fe5e3b00f9f1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "44.9"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "round((h/h1)*100,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "521c0682-21a3-4e3d-b0e4-c31829182522",
   "metadata": {},
   "outputs": [],
   "source": [
    "def calculate_demographic_data(print_data=True):\n",
    "    # Read data from file\n",
    "    df = pd.read_csv('adult.data.csv')\n",
    "    \n",
    "    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.\n",
    "    race_count = df['race'].value_counts()\n",
    "\n",
    "    # What is the average age of men?\n",
    "    average_age_men =round( df[df['sex']=='Male']['age'].mean(),1)\n",
    "\n",
    "    # What is the percentage of people who have a Bachelor's degree?\n",
    "    n= len(df[df['education']==\"Bachelors\"])\n",
    "    t=len(df)\n",
    "    percentage_bachelors =round((n/t)*100,1)\n",
    "\n",
    "    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?\n",
    "    # What percentage of people without advanced education make more than 50K?\n",
    "\n",
    "    # with and without `Bachelors`, `Masters`, or `Doctorate`\n",
    "    higher_education = df[df['education'].isin(['Bachelors','Masters','Doctorate'])]\n",
    "    lower_education = df[~df['education'].isin(['Bachelors','Masters','Doctorate'])]\n",
    "\n",
    "    # percentage with salary >50K\n",
    "    advanced_education_high_income=(higher_education[higher_education['salary']=='>50K'])\n",
    "    higher_education_rich = round(len(advanced_education_high_income)/len(higher_education)*100,1)\n",
    "    l=len(lower_education[lower_education['salary']=='>50K'])\n",
    "    lower_education_rich = round(l/len(lower_education)*100,1)\n",
    "\n",
    "    # What is the minimum number of hours a person works per week (hours-per-week feature)?\n",
    "    min_work_hours =df['hours-per-week'].min()\n",
    "\n",
    "    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?\n",
    "    m=df[df['hours-per-week']==min_work_hours]\n",
    "    s=m[m['salary']=='>50K']\n",
    "\n",
    "    rich_percentage = round((len(s)/len(m))*100,1)\n",
    "\n",
    "    # What country has the highest percentage of people that earn >50K?\n",
    "    high_income = df[df['salary'] == '>50K']\n",
    "    percentage_high_earning = (high_income['native-country'].value_counts() / df['native-country'].value_counts()) * 100\n",
    "    highest_earning_country =percentage_high_earning.idxmax()\n",
    "    highest_earning_country_percentage = round(percentage_high_earning.max(),1)\n",
    "\n",
    "    # Identify the most popular occupation for those who earn >50K in India.\n",
    "    indian_high_income =high_income[high_income['native-country']=='India']\n",
    "    top_IN_occupation = indian_high_income ['occupation'].value_counts().idxmax()\n",
    "    return {\n",
    "        'race_count': race_count,\n",
    "        'average_age_men': average_age_men,\n",
    "        'percentage_bachelors': percentage_bachelors,\n",
    "        'higher_education_rich': higher_education_rich,\n",
    "        'lower_education_rich': lower_education_rich,\n",
    "        'min_work_hours': min_work_hours,\n",
    "        'rich_percentage': rich_percentage,\n",
    "        'highest_earning_country': highest_earning_country,\n",
    "        'highest_earning_country_percentage':\n",
    "        highest_earning_country_percentage,\n",
    "        'top_IN_occupation': top_IN_occupation\n",
    "    }\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "75789396-fc42-475d-81c0-18af14bb5d28",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'race_count': race\n",
       " White                 27816\n",
       " Black                  3124\n",
       " Asian-Pac-Islander     1039\n",
       " Amer-Indian-Eskimo      311\n",
       " Other                   271\n",
       " Name: count, dtype: int64,\n",
       " 'average_age_men': 39.4,\n",
       " 'percentage_bachelors': 16.4,\n",
       " 'higher_education_rich': 46.5,\n",
       " 'lower_education_rich': 17.4,\n",
       " 'min_work_hours': 1,\n",
       " 'rich_percentage': 10.0,\n",
       " 'highest_earning_country': 'Iran',\n",
       " 'highest_earning_country_percentage': 41.9,\n",
       " 'top_IN_occupation': 'Prof-specialty'}"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "calculate_demographic_data()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f5e8f4a7-7831-4356-baa6-d3b5995454a6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "tensorflowgpu",
   "language": "python",
   "name": "tensorflowgpu"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
