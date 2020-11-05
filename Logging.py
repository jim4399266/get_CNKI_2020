import logging
class Logging():
    def __init__(self):
        logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',level=logging.INFO)
    def __call__(self, inputs):
        return logging.info(inputs)

log = Logging()
if __name__ == '__main__':
    log('test')