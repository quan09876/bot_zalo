IMEI = "71221225-749b-4e73-97d0-6c577e35da94-b78b4e2d6c0a362c418b145fe44ed73f"
SESSION_COOKIES = {"_ga":"GA1.2.1539186.1732438967","_zlang":"vn","app.event.zalo.me":"5357264775756627921","_gid":"GA1.2.2037388081.1733643983","zpsid":"COZS.427691510.3.kOEoKSbRb14_Lke8nLkK4RmevYNxRA8e-6wb8MAwHGpwjSoCoDB4HAvRb14","zpw_sek":"zI2o.427691510.a0.cIvL9X9lJpdaOZ4WCszFEMbDAb8mLMrzFGWzVtKv1H9TAXfSMYabKMKxFa1JKd8RRyIkw0zSeM6FRi5fHmXFEG"}
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