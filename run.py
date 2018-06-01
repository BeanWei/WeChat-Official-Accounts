import logging
from logging.handlers import RotatingFileHandler

from app import config, app


#日志记录
handler = RotatingFileHandler("./logs/app.log", maxBytes=10000, backupCount=1)
handler.setFormatter(logging.Formatter(
    "%(asctime)s %(levelname)s: %(message)s"
    "[in %(pathname)s:%(lineo)d]"
))
app.logger.addHandler(handler)


if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT)