import time
from zlapi.models import Message, ThreadType
from config import ADMIN

des = {
    'version': "1.0.2",
    'credits': "Nguyễn Đức Tài",
    'description': "Gửi spam công việc cho người dùng được tag"
}

def handle_spamtodo_command(message, message_object, thread_id, thread_type, author_id, client):
    if author_id not in ADMIN:
        client.replyMessage(
            Message(text="Quyền lồn biên giới"),
            message_object, thread_id, thread_type
        )
        return

    parts = message.split(' ', 3)
    
    if len(parts) < 4:
        response_message = "Vui lòng cung cấp uid, nội dung và số lần spam công việc. Ví dụ: spamtodo <uid> Nội dung công việc 5"
        client.replyMessage(Message(text=response_message), message_object, thread_id, thread_type)
        return

    tagged_user = parts[1]
    content = parts[2]
    try:
        num_repeats = int(parts[3])
    except ValueError:
        response_message = "Số lần phải là một số nguyên."
        client.replyMessage(Message(text=response_message), message_object, thread_id, thread_type)
        return

    for _ in range(num_repeats):
        client.sendToDo(
            message_object=message_object,
            content=content,
            assignees=[tagged_user],
            thread_id=tagged_user,
            thread_type=ThreadType.USER,
            due_date=-1,
            description="Soiz"
        )
        time.sleep(0.2)

def get_szl():
    return {
        'spamtodo': handle_spamtodo_command
    }
