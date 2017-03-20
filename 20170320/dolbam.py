# -*- coding:utf-8 -*-

import logging
logging.basicConfig(filename='./dolbam.log',level=logging.DEBUG)
#logging.basicConfig(level=logging.DEBUG)

log_file = './dolbam.log'
log_level = 'DEBUG'
log_format = '[%(asctime)s: '

logging.debug("디버깅을 위한 메시지 로그")
logging.info("정보를 제공하기 위한 메시지 로그")
logging.warning("주의해야할 사항들")
logging.error("에러 발생!")
logging.critical("심각한 에러!!")