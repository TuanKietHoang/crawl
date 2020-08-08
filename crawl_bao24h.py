import scrapy

class TuoiTre(scrapy.Spider):
    name = 'bao24h'
    allowed_domains = ['24h.com.vn']
    start_urls = ['https://www.24h.com.vn/']
    count = 0
    def parse(self, response):
        f = open('C:\\Users\\Admin\\PycharmProjects\\bao24h\\tutorial\\tutorial\\spiders\\Output\\bao24h_output.txt', 'a',
                 encoding='utf-8')
        if response.status == 200 and response.css('meta[property="og:type"]::attr("content")').get() == 'article':

            Link = response.url
            f.write('[ Source_Link : ' + str(Link).strip() + '\n')
            f.write('\n')

            Time = response.css('div[class="updTm updTmD mrT5"]::text').getall()
            f.write('Time : ' + str(Time) + '\n')
            f.write('\n')


            Event = response.css('div.sbNws')
            f.write('Event : ' + ''.join(Event.css('a *::text').getall()).strip() + '\n')
            f.write('\n')

            Title = response.css('h1[id="article_title"]::text').get()
            f.write('Title : ' + str(Title).strip() + '\n')
            f.write('\n')

            Article_sapo = response.css('h2[id="article_sapo"]::text').get()
            f.write('Article_Sapo : ' + str(Article_sapo).strip() + '\n')
            f.write('\n')

            f.write('Content : ')
            for i in response.css('article[id="article_body"] p'):
                content = ''.join(i.css('*::text').getall())
                f.write( str(content).strip() + '\n')

            Author = response.css('div[class="nguontin nguontinD bld mrT10 mrB10 fr"]')
            f.write('Author : ' + ''.join(Author.css('*::text').getall()).strip() + '\n' + ' ]')
            f.write('\n')

            self.count += 1
            self.crawler.stats.set_value('CRAWL COUNT', self.count)

        yield from response.follow_all(css='a[href^="https://www.24h.com.vn/"]::attr(href)', callback=self.parse)