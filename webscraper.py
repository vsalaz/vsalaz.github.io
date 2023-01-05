import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/valentinsalazar/Desktop/WebDriver/chromedriver')
driver.get('https://www.nytimes.com/section/sports')
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

for a in soup.find_all(attrs='css-1l4spti'):
    article = a.find('h2')
    if article not in results:
        results.append(article.text)

print(results)
for b in soup.find_all(attrs='css-agsgss e15t083i3'):
    date = b.find('span')
    if date not in other_results:
        other_results.append(date.text)

print(other_results)
df = pd.DataFrame({'Articles': results, 'Date': other_results})
df.to_csv('nytimes.csv', index=False, encoding='utf-8')


