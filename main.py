import requests
import re
from bs4 import BeautifulSoup
from datetime import date, timedelta
from collections import Counter
from string import punctuation

URL = "https://blog.hubspot.com/"


def check_most_recent_blogs(check_older_blogs: int = 0) -> str:
    """
    Purpose: 
    Checks current date for finding the most recent blog entries.

    Input:
    check_older_blogs (int): In case there are not enough of most recent
    blog entries, check the older ones.

    Output: 
    current_date_formated (str): String representation of current date.
    check_older_blogs (int): Allows to change parameter.
    """
    current_date = date.today()
    current_date = current_date - timedelta(days=check_older_blogs)
    current_date_formated = current_date.strftime("%m/%d/%y")
    return current_date_formated, check_older_blogs


def fetch_blogs(
        number_of_articles_to_fetch: int,
        current_date_formated: str,
        check_older_blogs: int
    ) -> list[str]: 
    """
    Purpose:
    Scrapes the homepage of website provided in the global constant "URL"
    by looking through HTML code, seeking the blogs posting dates.

    Input:
    number_of_articles_to_fetch (int): Variable to imply, how many articles we
    want to search for.
    current_date_formated (str): String representation of current date.
    check_older_blogs (int): In case there are not enough recent articles,
    start looking for older ones.

    Output:
    URLs (list[str]): list of URLs of <number_of_articles_to_fetch>
    most recent blogs posted on website
    """
    html_text = requests.get(URL).text
    soup = BeautifulSoup(html_text, "lxml")
    blogs = soup.find_all("li", class_="blog-categories-post")
    URLs = list()

    while number_of_articles_to_fetch != 0:
        for blog in blogs:
            if number_of_articles_to_fetch == 0:
                break
            posting_date_div = blog.div.div.div
            posting_date = posting_date_div.find_all("p")[1].text.split()[0]

            if posting_date in current_date_formated:
                URL_to_blog = blog.div.div.h3.a["href"]
                URLs.append(URL_to_blog)
                number_of_articles_to_fetch -= 1

        check_older_blogs += 1
        current_date_formated = check_most_recent_blogs(
            check_older_blogs=check_older_blogs)[0]

    return URLs


def analyze_blogs(URLs: list[str]):
    """
    Purpose:

    Input:
    
    Output:
    """
    for url in URLs:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'lxml')
            blog_title = soup.find("span", class_="hs_cos_wrapper hs_cos_wrapper_meta_field hs_cos_wrapper_type_text").text

            text = soup.get_text()
            words = re.findall(r'\b\w+\b', text.lower())
            word_counts = Counter(words)
            most_common_words = word_counts.most_common(5)
            
            # Print the results
            print(f"\nBlog title: \"{blog_title}\"")
            print(f"Blog URL: \"{url}\"")
            print(f"All words count: {len(words)}")
            print(f"All characters count: {len(text)}")
            print(f"Most frequent words in blog:")
            for word, count in most_common_words:
                print(f'{word}: {count}')
        

def main():
    number_of_articles_to_fetch = 3
    current_date_formated, check_older_blogs = check_most_recent_blogs()
    URLs = fetch_blogs(
        number_of_articles_to_fetch,
        current_date_formated,
        check_older_blogs
    )
    analyze_blogs(URLs)
    

if __name__ == "__main__":
    main()