from datetime import datetime

def get_greeting():
    # Поточний час із мілісекундами
    current_time = datetime.now().isoformat()
    # Формуємо повідомлення
    greeting_message = "Welcome to the Internet Andriy Strilets, have a little fun."
    
    # Повертаємо повідомлення та час
    return greeting_message, current_time
