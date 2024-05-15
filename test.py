import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta

URL = "https://blog.hubspot.com/"


def check_most_recent_blogs(check_older_blogs: int = 0) -> str:
    """
    Purpose: 
    Checks current date for finding the most recent blog entries

    Input:
    check_older_blogs (int): In case there are not enough of most recent
    blog entries, check the older ones

    Output: 
    current_date_formated (str): string representation of current date
    """
    current_date = date.today()
    current_date = current_date - timedelta(days=check_older_blogs)
    current_date_formated = current_date.strftime("%m/%d/%y")

    print(f"Current date: {current_date_formated}")
    return current_date_formated, check_older_blogs


def fetch_blogs(number_of_articles_to_fetch, current_date_formated, check_older_blogs):
    """
    Purpose:
    Scrapes the homepage of website provided in the global constant "URL"
    and return 

    Input:
    current_date_formated (str): string representation of current date

    Output:
    URLs (list): list of URLs of three most recent blogs posted on website
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
                print("One of the most recent article is fetched")
                URL_to_blog = blog.div.div.h3.a["href"]
                URLs.append(URL_to_blog)
                number_of_articles_to_fetch -= 1

        check_older_blogs += 1
        current_date_formated = check_most_recent_blogs(check_older_blogs=check_older_blogs)[0]

    return URLs


def main():
    number_of_articles_to_fetch = 3
    current_date_formated, check_older_blogs = check_most_recent_blogs()
    URLs = fetch_blogs(number_of_articles_to_fetch, current_date_formated, check_older_blogs)
    print(URLs)
    







    # with open("home.html", "r") as html_file:
    # # with open("blog.html", "r") as html_file:
    #     content = html_file.read()
    #     soup = BeautifulSoup(content, "lxml")
    #     # courses_html_tags = soup.find_all("h5")
    #     # # courses_html_tags = soup.find_all("p")
    #     # for course in courses_html_tags:
    #     #     print(course.text)
    #     course_cards = soup.find_all("div", class_="card")
    #     for course in course_cards:
    #         course_name = course.h5.text
    #         course_price = course.a.text.split()[-1]

    #         print(f"{course_name} costs {course_price}")


    # with open("main.html", "r") as html_file:
    #     content = html_file.read()
    #     soup = BeautifulSoup(content, "lxml")
    #     # date_times = soup.find_all("time", class_="blog-post-card-date")
    #     blogs_entries = soup.find("li", class_="blog-categories-post")
    #     for index, blog in enumerate(blogs_entries):
    #         href = soup.find("a", href)
    #         # print(blogs_entries)
    #         print(href)
    #         # published_date = blog.find("/")
    #         # print(published_date)
    #     # href = date_times.
    #     # for date_ in date_times:
    #     #     print(date_)



if __name__ == "__main__":
    main()