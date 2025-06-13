IMEI = "901ce41d-5f18-41ce-a924-c6aa8cfb9638-f318d71f51e2f42138d3a75f6a7137a8"
SESSION_COOKIES = "{"url":"https://chat.zalo.me","cookies":[{"domain":".zalo.me","expirationDate":1784338221.708144,"hostOnly":false,"httpOnly":false,"name":"_ga","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"GA1.2.207009874.1748840171"},{"domain":".zalo.me","expirationDate":1780882221,"hostOnly":false,"httpOnly":false,"name":"ZConsent","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"timestamp=1748840179758&location=https://zalo.me/pc"},{"domain":".chat.zalo.me","expirationDate":1780882238,"hostOnly":false,"httpOnly":false,"name":"ZConsent","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"timestamp=1748840179758&location=https://zalo.me/pc"},{"domain":".zalo.me","expirationDate":1784338238.999764,"hostOnly":false,"httpOnly":false,"name":"__zi","path":"/","sameSite":"no_restriction","secure":true,"session":false,"storeId":"0","value":"3000.SSZzejyD0jydXQckra00a3BBfxQL71AQV8UZjzXL5ffqWAlwqL0Qtds3h_FHL1hSCm.1"},{"domain":".zalo.me","expirationDate":1784338238.999977,"hostOnly":false,"httpOnly":false,"name":"__zi-legacy","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"3000.SSZzejyD0jydXQckra00a3BBfxQL71AQV8UZjzXL5ffqWAlwqL0Qtds3h_FHL1hSCm.1"},{"domain":".zalo.me","expirationDate":1783400282.434331,"hostOnly":false,"httpOnly":false,"name":"ozi","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"2000.SSZzejyD0jydXQckra00a3BBfxQK71AQVOUaiTrH59jyXAItsHyGd7d0hRJT5X2OC3Cp.1"},{"domain":".zalo.me","expirationDate":1784099539.056158,"hostOnly":false,"httpOnly":false,"name":"_ga_VM4ZJE1265","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"GS2.2.s1749539535$o1$g1$t1749539539$j56$l0$h0"},{"domain":".zalo.me","expirationDate":1781075592.586483,"hostOnly":false,"httpOnly":true,"name":"zpsid","path":"/","sameSite":"no_restriction","secure":true,"session":false,"storeId":"0","value":"42tq.410501828.1.RdJTEKY95SECIsBRH8aLmptwP_TvkI3pUR4d-qOscPrwU3TYIO7EX2295SC"},{"domain":".chat.zalo.me","expirationDate":1750144393.505631,"hostOnly":false,"httpOnly":true,"name":"zpw_sek","path":"/","sameSite":"lax","secure":true,"session":false,"storeId":"0","value":"vMlp.410501828.a0.90lBdJkjPll_Rn7Z6grc-q2F0v0PbqJARVKNacB82uDGdJJFOvytcbJKCQbSa5lPHgFPTsMVbzcQh6yWVCLc-m"},{"domain":".zalo.me","expirationDate":1749864621,"hostOnly":false,"httpOnly":false,"name":"_gid","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"GA1.2.99648646.1749778222"},{"domain":".zalo.me","expirationDate":1749778281,"hostOnly":false,"httpOnly":false,"name":"_gat","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"1"},{"domain":".zalo.me","expirationDate":1784338222.730811,"hostOnly":false,"httpOnly":false,"name":"_ga_RYD7END4JE","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"GS2.2.s1749778222$o3$g1$t1749778222$j60$l0$h0"},{"domain":".zalo.me","expirationDate":1749864634.395814,"hostOnly":false,"httpOnly":false,"name":"_zlang","path":"/","sameSite":"unspecified","secure":true,"session":false,"storeId":"0","value":"vn"},{"domain":".zalo.me","expirationDate":1749951039.496642,"hostOnly":false,"httpOnly":true,"name":"app.event.zalo.me","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"8655461523095210903"}]}"
API_KEY = "api_key"
SECRET_KEY = "secret_key"
PREFIX = "!"






import re
import os
import json
SETTING_FILE= "setting.json"
#Không chỉnh sửa nếu bạn không có kinh nghiệm
def read_settings():
    """Đọc toàn bộ nội dung từ file JSON."""
    try:
        with open(SETTING_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def write_settings(settings):
    """Ghi toàn bộ nội dung vào file JSON."""
    with open(SETTING_FILE, 'w', encoding='utf-8') as file:
        json.dump(settings, file, ensure_ascii=False, indent=4)


def is_admin(author_id):
    settings = read_settings()
    admin_bot = settings.get("admin_bot", [])
    if author_id in admin_bot:
        return True
    else:
        return False
def get_user_name_by_id(bot,author_id):
    try:
        user = bot.fetchUserInfo(author_id).changed_profiles[author_id].displayName
        return user
    except:
        return "Unknown User"

def handle_bot_admin(bot):
    settings = read_settings()
    admin_bot = settings.get("admin_bot", [])
    if bot.uid not in admin_bot:
        admin_bot.append(bot.uid)
        settings['admin_bot'] = admin_bot
        write_settings(settings)
        print(f"Đã thêm 👑{get_user_name_by_id(bot, bot.uid)} 🆔 {bot.uid} cho lần đầu tiên khởi động vào danh sách Admin 🤖BOT ✅")

settings= read_settings()
ADMIN = [settings.get("admin_bot", [])]
