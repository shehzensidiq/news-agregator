import requests
from bs4 import BeautifulSoup
# newsFile = open("News.txt","a")
baseUrl = 'https://www.cnet.com'
def getNews(url):
    newsList = []
    #html
    page = requests.get(url)
    #bs4
    soupObject = BeautifulSoup(page.content, "html.parser")

    news = soupObject.find_all("div", class_ = "row asset")
    for result in news:
        title = result.find("h2")
        # intro = result.find("p")
        if None == title:
            continue
        link = result.find("a")["href"]
        if 'videos' in link:
            continue
        link = baseUrl + link
        # newsPage = requests.get(link).content
        # newsPageSoup = BeautifulSoup(newsPage,"html.parser")
        # mainBody1 = newsPageSoup.find("p", class_="speakableTextP1").text.strip()
        # mainBody2 = newsPageSoup.find("p", class_="speakableTextP2").text.strip()
        # mainBody1 = ".\n".join(mainBody1.split("."))
        # mainBody2 = ".\n".join(mainBody2.split("."))  'body':mainBody1,

        # newsBody = mainBody1 + "\n" + mainBody2
        newsList.append({'title': title.text.strip(), 'link': link})
        if len(newsList) == 11:
            break
        # # print(mainBody1 + "\n\n"+mainBody2)
        # newsFile.write("Title:\n" + title.text.strip()+"\n")
        # newsFile.write("Description:\n" + newsBody + "\n\n")
        # newsList.append({'title': title.text.strip(), 'link': link})

    return newsList

#greater kashmir
def get_gk_news(url):

    gk_news_list = []
    page = requests.get(url).content
    gk_soup = BeautifulSoup(page,"html.parser")
    latest_news_list = gk_soup.find_all("div", class_="type-post")

    for post in latest_news_list:
        title = post.find("h2")
        if title == None:
            continue
        title = title.text.strip()
        link = post.find("a")["href"]
        #each page vsist
        # each_page_html = requests.get(link)
        # each_page = BeautifulSoup(each_page_html.content, "html.parser")
        # news_content = each_page.find("p").text---'body': news_content[:200]
        gk_news_list.append({'title': title, 'link': link})
        if len(gk_news_list) == 11:
            break
    return gk_news_list

#jobs in kashmir
def get_jobs():
    job_list = []
    response = requests.get("https://jkadworld.com/category/jammu-kashmir-jobs/")

    jobs_soup = BeautifulSoup(response.content, "html.parser")
    jobs = jobs_soup.find_all("div", class_="article-content")

    for job in jobs:
        last_date = None
        total_posts = None
        header = job.find("h2")
        if header == None:
            continue
        link = header.find("a")["href"]
    # sep pages
        detail_page = requests.get(link)
        detail_page_soup = BeautifulSoup(detail_page.content, "html.parser")

        # details of job
        container = detail_page_soup.find("div", class_="entry-content")
        details = container.find_all("p")
        if details == None:
            continue
        for detail in details:
            if 'Total no of Posts' in detail.text:
                total_posts = detail.text.strip()
            if 'Last Date' in detail.text:
                last_date = detail.text.strip()
        job_list.append({'title': header.text.strip(), 'link': link, 'last_date': last_date, 'total_posts': total_posts})
        if len(job_list) == 8:
            break
    return job_list




