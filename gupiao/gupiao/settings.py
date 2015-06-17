# -*- coding: utf-8 -*-

# Scrapy settings for gupiao project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'gupiao'

SPIDER_MODULES = ['gupiao.spiders']
NEWSPIDER_MODULE = 'gupiao.spiders'
ITEM_PIPELINES = ['gupiao.pipelines.GupiaoPipeline',
                ]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'gupiao (+http://www.yourdomain.com)'

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:7.0.1) Gecko/20100101 Firefox/7.7'

DOWNLOAD_TIMEOUT = 15
# DOWNLOAD_DELAY = 0.1
# LOG_LEVEL = "INFO"
# LOG_STDOUT = True
# LOG_FILE = "log/newsSpider.log"