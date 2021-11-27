# ログ出力
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.debug('デバッグ出力')
logger.info('情報出力')
logger.warning('警告出力')
logger.error('エラー出力')
logger.critical('致命的エラー出力')
