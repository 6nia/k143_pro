import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7949227263:AAGqSx4PiF2loVT8GGTPSU3OxaIRaXI8ahA")
API_ID = int(os.environ.get("API_ID", "18489236"))
API_HASH = os.environ.get("API_HASH", "f69613814cdb130946c5f20acbef3d56")
SPOILER_MODE = bool(os.environ.get("SPOILER_MODE", True))