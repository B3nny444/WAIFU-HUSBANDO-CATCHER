class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "1513565142"
    sudo_users = "1513565142", "7190881436"
    GROUP_ID = -1002220356089
    TOKEN = "7008178074:AAHRxTvWF_HBlQ-FXzg5gnYhXzHpmLWEj5A"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "Collect_em_support"
    UPDATE_CHAT = "Collect_em_support"
    BOT_USERNAME = "Collect_Em_AllBot"
    CHARA_CHANNEL_ID = "-1002220356089"
    api_id = 27094161
    api_hash = "39477b23f5e6abea95fe0f92b7f00de0"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
