import logging
import os
from datetime import datetime

from us_visa.utils.common import from_root  # ✅ Correct import

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_dir = 'logs'

logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

# ✅ Make sure the full log path's directories exist
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

# ✅ Logging configuration
logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)
