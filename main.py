import requests
import pandas as pd
from bs4 import BeautifulSoup
from textblob import TextBlob

# Base URL and query parameters
base_url = "https://www.airlinequality.com/airline-reviews/british-airways"
pages = 36
page_size = 100

reviews = []

review_data_list = []

for i in range(1, pages + 1):
    # Create URL to collect links for paginated data
    url = f"{base_url}/page/{i}/?sortby=post_date%3ADesc&pagesize={page_size}"

    # Collect HTML data from this page
    response = requests.get(url)

    # Parse content
    content = response.content
    parsed_content = BeautifulSoup(content, 'html.parser')

    # Find and extract review elements on the page
    review_elements = parsed_content.find_all('div', class_='body')
    a_elements = parsed_content.find_all('a', class_='toggle-click tc_mobile_only')

    for review_element, a_element in zip(review_elements, a_elements):
        # Extract specific data elements from each review element
        review_title = review_element.find('h2', class_='text_header').text
        customer_name = review_element.find('span', itemprop='name').text
        country_full = review_element.find('span', itemprop='author').parent.text.strip()

        # Extract only the country part
        country_start = country_full.find("(")
        country_end = country_full.find(")")
        country = country_full[country_start + 1: country_end].strip()
        date = review_element.find('time', itemprop='datePublished')['datetime']

        # Extract the ID attribute value from the <a> element
        customer_id = a_element.get('href')
        review_text = review_element.find('div', itemprop='reviewBody').text

        # Perform sentiment analysis using TextBlob
        analysis = TextBlob(review_text)
        sentiment = analysis.sentiment.polarity  # Range from -1 (negative) to 1 (positive)

        # Extract recommended status
        recommended_element = review_element.find('td', class_='review-value rating-no')
        recommended = recommended_element.text.strip() if recommended_element else ''

        # Create a dictionary to store review data
        review_data = {
            "Review Title": review_title,
            "Customer Name": customer_name,
            "Customer Id": customer_id,
            "Country": country,
            "Date": date,
            "Recommended": recommended,
            "Sentiment": sentiment,
        }

        # Append the review_data to the list
        review_data_list.append(review_data)

# Create a DataFrame from the list of review_data
df = pd.DataFrame(review_data_list)

# Print the DataFrame
print(df)

# Assuming you already have your DataFrame df
# Export the DataFrame to a CSV file
# df.to_csv('British_Airways.csv', index=False)