import requests
from bs4 import BeautifulSoup
from flask import Flask,render_template
from functions import getNews, get_gk_news, get_jobs

app = Flask(__name__)

#url startups
url = 'https://www.cnet.com/topics/security/'
googleUrl = 'https://www.cnet.com/google/'
appleUrl = 'https://www.cnet.com/apple/'
computersUrl = 'https://www.cnet.com/topics/computers/'
cultureUrl = 'https://www.cnet.com/topics/culture/'
internetUrl = 'https://www.cnet.com/topics/internet/'
microsoftUrl = 'https://www.cnet.com/tags/microsoft/'
mobileUrl = 'https://www.cnet.com/topics/mobile/'
sciTechUrl = 'https://www.cnet.com/topics/sci-tech/'
techIndUrl = 'https://www.cnet.com/topics/tech-industry/'

@app.route("/")
def index():
    newsPart = getNews(url)
    greater_kashmir = get_gk_news('https://www.greaterkashmir.com/latest/')
    jobs = get_jobs()
#     return render_template("index.html", gk_news = newsPart, title = "Greater Kashmir")
    return render_template("index.html", newsFetched = newsPart, title = "Security",gk_title = 'Greater Kashmir', jobs_title = 'Jobs',gk_news = greater_kashmir, jobs = jobs)

@app.route("/google")
def google():
    newsPart = getNews(googleUrl)
    return render_template("index.html", newsFetched = newsPart, title = 'Google')

@app.route("/apple")
def apple():
    newsPart = getNews(appleUrl)
    return render_template("index.html", newsFetched = newsPart, title = 'Apple')


@app.route('/computers')
def computers():
    newsPart = getNews(computersUrl)
    return render_template("index.html", newsFetched = newsPart, title = 'Computers')


@app.route('/culture')
def culture():
    newsPart = getNews(cultureUrl)
    return render_template("index.html", newsFetched = newsPart, title = 'Culture')


@app.route('/internet')
def internet():
    newsPart = getNews(internetUrl)
    return render_template("index.html", newsFetched = newsPart, title = 'Internet')


@app.route('/microsoft')
def microsoft():
    newsPart = getNews(microsoftUrl)
    return render_template("index.html", newsFetched = newsPart, title = 'Microsoft')


@app.route('/mobile')
def mobile():
    newsPart = getNews(mobileUrl)
    return render_template("index.html", newsFetched = newsPart, title = 'Mobile')


@app.route('/sci-tech')
def sci_tech():
    newsPart = getNews(sciTechUrl)
    return render_template("index.html", newsFetched = newsPart, title = 'Sci-Tech')


@app.route('/tech-industry')
def tech_industry():
    newsPart = getNews(techIndUrl)
    return render_template("index.html", newsFetched = newsPart, title = 'Tech Industry')


if __name__ == '__main__':
    app.run()