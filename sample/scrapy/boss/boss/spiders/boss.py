import scrapy,bs4,time
from ..items import BossItem

class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domins = ['https://www.zhipin.com/']
    start_urls = []
    for p in range(1,11):
        url = 'https://www.zhipin.com/c101020100/?query=php&page=' + str(p) + '&ka=page-' + str(p)
        start_urls.append(url)

    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text,'html.parser')
        datas = soup.find_all('div',class_ = 'job-primary')
        for data in datas:
            job_detail_url = data.find('div', class_ = 'info-primary').find('a')['href']
            real_job_detail_url = 'https://www.zhipin.com' + job_detail_url
            yield scrapy.Request(real_job_detail_url, callback = self.parse_job_detail)
            # time.sleep(3)
        # time.sleep(3)

    def parse_job_detail(self, response):
        soup = bs4.BeautifulSoup(response.text,'html.parser')
        company = soup.find('a', ka = 'job-detail-company')['title']
        job_title = soup.find('div', class_ = 'job-primary detail-box').find('div', class_ = 'info-primary').find('h1').text
        job_salary = soup.find('div', class_ = 'job-primary detail-box').find('div', class_ = 'info-primary').find('span', class_ = 'salary').text.strip()
        job_info = soup.find('div', class_ = 'job-primary detail-box').find('div', class_ = 'info-primary').find('p').text
        job_description = soup.find('div',class_ = 'detail-content').find('div', class_ = 'text').text
        item = BossItem()
        item['company'] = company
        item['job_title'] = job_title
        item['job_salary'] = job_salary
        item['job_info'] = job_info
        item['job_description'] = job_description
        yield item
