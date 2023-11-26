import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6698833829:AAEB0ebmvUNOcU4J6ubcOadokaUVqGl7mBE")

    APP_ID = int(os.environ.get("APP_ID", 25603034))

    API_HASH = os.environ.get("API_HASH", "294a7bf4488b21609436de1cdd05c316")
