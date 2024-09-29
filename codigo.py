import pandas as pd

def analyze_demographic_data():
    data = pd.read_csv('path/to/dataset.csv')

    race_count = data['race'].value_counts()

    average_age_men = data[data['sex'] == 'Male']['age'].mean()

    bachelors_percentage = (data['education'].value_counts(normalize=True)['Bachelors'] * 100).round(1)

    advanced_education = data[data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    percentage_advanced_50K = (advanced_education[advanced_education['salary'] == '>50K'].shape[0] / advanced_education.shape[0] * 100).round(1)

    non_advanced_education = data[~data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    percentage_non_advanced_50K = (non_advanced_education[non_advanced_education['salary'] == '>50K'].shape[0] / non_advanced_education.shape[0] * 100).round(1)

    min_hours_per_week = data['hours-per-week'].min()

    min_hours_salary = data[data['hours-per-week'] == min_hours_per_week]
    percentage_min_hours_50K = (min_hours_salary[min_hours_salary['salary'] == '>50K'].shape[0] / min_hours_salary.shape[0] * 100).round(1)

    country_salary = data[data['salary'] == '>50K']['native-country'].value_counts(normalize=True) * 100
    highest_percentage_country = country_salary.idxmax()
    highest_percentage_value = country_salary.max().round(1)

    popular_occupation_india = data[(data['native-country'] == 'India') & (data['salary'] == '>50K')]['occupation'].mode()[0]

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'bachelors_percentage': bachelors_percentage,
        'percentage_advanced_50K': percentage_advanced_50K,
        'percentage_non_advanced_50K': percentage_non_advanced_50K,
        'min_hours_per_week': min_hours_per_week,
        'percentage_min_hours_50K': percentage_min_hours_50K,
        'highest_percentage_country': highest_percentage_country,
        'highest_percentage_value': highest_percentage_value,
        'popular_occupation_india': popular_occupation_india,
    }

if __name__ == '__main__':
    results = analyze_demographic_data()
    print(results)