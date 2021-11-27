import logging

# ログファイル出力
# ハンドラーを作成
std_handler = logging.StreamHandler()
file_handler = logging.FileHandler('basic/basic3.log')

# フォーマット、レベル、ハンドラーを指定
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO, handlers=[std_handler, file_handler])
logger = logging.getLogger(__name__)
logger.debug('デバッグ出力')
logger.info('情報出力')
logger.warning('警告出力')
logger.error('エラー出力')
logger.critical('致命的エラー出力')
