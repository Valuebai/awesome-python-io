#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@IDE    ：PyCharm
@Author ：LuckyHuibo
@Date   ：2019/9/2 11:35
@Desc   ：
=================================================='''
import logging
import sys
import warnings

logger = logging.getLogger(__name__)

logging.basicConfig(
    format='%(asctime)s : %(threadName)s : %(levelname)s : %(message)s',
    level=logging.INFO
)

_MIGRATION_NOTES_URL = (
    'https://github.com/RaRe-Technologies/smart_open/blob/master/README.rst'
    '#migrating-to-the-new-open-function'
)

if __name__ == "__main__":
    # print(sys.argv[0])
    # print(sys.argv)

    logger.info("running %s", " ".join(sys.argv))

    warnings.warn(
        'This function is deprecated, use smart_open.open instead. '
        'See the migration notes for details: %s' % _MIGRATION_NOTES_URL
    )
