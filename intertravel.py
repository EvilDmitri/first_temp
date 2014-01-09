import urllib
from grab.spider import Spider, Task, Data
from grab.tools.files import hashed_path_details

import os

import locale
enc = locale.getpreferredencoding()

BASE_PAGE = 'http://www.intertravel.dk/'
START = '1'
#directory = '../images/'

import logging
logging.basicConfig(level=logging.DEBUG)

class KinoSpider(Spider):

    def task_generator(self):
        for x in range(int(START), int(START)+1):
            page = BASE_PAGE + 'traveloffer.cfm?nSupplierId=87&nModuleType=1&npage=' + str(x)
            yield Task('initial', url=page)

    def task_initial(self, grab, task):
        for title in grab.xpath_list('//div[@class="button_right"]'):
            link = BASE_PAGE + title[0].get('href')
            print link
            self.add_task(Task('hop', url=link))

    def task_hop(self, grab, task):
        url = {}
        title = {}
        reisemal = {}
        afreise = {}
        varighed = {}
        pris = {}
        af_periode = {}
        overnatning = {}
        transport = {}
        description = {}
        category = {}

        reisetype = {}
        dagsprogram = {}
        images = {}
        prices = {}

        inkluderer = {}
        other = {}


        # url =
        title = grab.xpath('//h1').text()


        data = [

        ]
        output = ')'
        with open('data.db', 'a') as f:
            f.write(output.encode('utf-8') + '\n')


def main():

    # Create directory for images
    #if not os.path.exists(directory):
    #    os.makedirs(directory)

    threads = 1

    bot = KinoSpider(thread_number=threads,network_try_limit=10)

    try: bot.run()
    except KeyboardInterrupt: pass

    print bot.render_stats()

if __name__ == '__main__':
    main()


