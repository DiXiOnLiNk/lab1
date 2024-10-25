from flask import Flask, render_template_string
from service import get_greeting

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    # Отримуємо привітання через сервіс
    greeting_message, time_of_refresh = get_greeting()
    # Шаблон HTML для відповіді
    html_template = """
    <html>
        <body>
            <p>{{ message }} Time of last refresh:{{ time }}</p>
        </body>
    </html>
    """
    # Рендеримо HTML з даними
    return render_template_string(html_template, message=greeting_message, time=time_of_refresh)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
