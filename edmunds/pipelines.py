# -*- coding: utf-8 -*-

import os
import json
from scrapy.utils.serialize import ScrapyJSONEncoder

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class EdmundsPipeline(object):
    path_prefix = "makes"
    encoder = ScrapyJSONEncoder()

    def process_item(self, item, spider):
        make_path = os.path.join(self.path_prefix, item['make'])
        if not os.path.exists(make_path):
            os.makedirs(make_path)

        model_path = os.path.join(make_path, item['model'])
        if not os.path.exists(model_path):
            os.makedirs(model_path)

        year_path = os.path.join(model_path, item['year'])
        if not os.path.exists(year_path):
            os.makedirs(year_path)

        file_path = os.path.join(year_path, item['style'] + '.json')

        with open(file_path, 'w') as f:
            f.write(self.encoder.encode(item))

        return item
