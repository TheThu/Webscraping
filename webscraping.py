from bs4 import BeautifulSoup
import requests

###### Scrape cola price data from different cities #######

# define variable #
city_1 = 'Hamburg'
city_2 = 'Leipzig'

# f, format String 

url =f'https://www.numbeo.com/cost-of-living/compare_cities.jsp?country1=Germany&country2=Germany&city1={city_1}&city2={city_2}&tracking=getDispatchComparison'

#store request from url in data
page =requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#find data soup with class 'data_wide_table new_bar_table cost_comparison_table'#
table = soup.find('table',attrs={'class':'data_wide_table new_bar_table cost_comparison_table'})


# finde all rows
rows = table.find_all('tr')

cola_data = rows[7].text.split();

price_1 = cola_data[4]
price_2 = cola_data[6]

# print out price data
print(f'Der Colapreis in {city_1} betraegt {price_1} €')
print(f'Der Colapreis in {city_2} betraegt {price_2} €')


