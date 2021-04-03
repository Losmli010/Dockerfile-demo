from utils import log


logger = log.get_logger(__name__)


def reply(request):
    logger.info('request name: %s', request.name)
    if request.name == 'losmli':
        result = {'message': '人之初，性本善。'}
    else:
        result = {'message': '天行健，君子以自强不息。地势坤，君子以厚德载物。'}
    logger.info('response: %s', result)
    return result
