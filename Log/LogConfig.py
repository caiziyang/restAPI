import logging

logging.basicConfig(level=logging.DEBUG,format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename= 'D:\\software\\selenium\PyCode\\test_api_framework\\test_Log\\log.txt',
                    filemode='a'),  # log格式',)