# -*- coding: utf-8 -*-

# Scrapy settings for edmunds project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'edmunds'

SPIDER_MODULES = ['edmunds.spiders']
NEWSPIDER_MODULE = 'edmunds.spiders'

DOWNLOAD_DELAY = 2

ITEM_PIPELINES = {
    'edmunds.pipelines.EdmundsPipeline': 500
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'edmunds (+http://www.yourdomain.com)'
