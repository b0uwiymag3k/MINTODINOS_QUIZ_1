#6541829338:AAHftopC_mKOU3xFCHnlxAN24I789hoXobY
#1281869576
import telebot
from telebot import types

# Создаем экземпляр бота
bot = telebot.TeleBot('6541829338:AAHftopC_mKOU3xFCHnlxAN24I789hoXobY')
good = 0
user_info = None
q = []
prev_question_message_id = None

# Список вопросов и ответов
questions = [
    {"question": "Какой из этих динозавров был хищником? 🦖", "answers": ["a) Трицератопс", "b) Стегозавр", "c) Велоцираптор", "d) Брахиозавр"], "correct": "c) Велоцираптор"},
    {"question": "Какой период является поздним для появления динозавров? 🌎", "answers": ["a) Триасовый", "b) Юрский", "c) Меловой", "d) Палеозойский"], "correct": "d) Палеозойский"},
    {"question": "Какой динозавр считается самым большим из всех? 🦕", "answers": ["a) Тираннозавр Рекс", "b) Спинозавр", "c) Аргентинозавр", "d) Аллозавр"], "correct": "c) Аргентинозавр"},
    {"question": "Какое из этих мест является наиболее известным археологическим местом динозавров? 🏞️", "answers": ["a) Долина Чеди", "b) Монумент Долина Огня", "c) Петрифицированный лес", "d) Гранд Каньон"], "correct": "a) Долина Чеди"},
    {"question": "Какое растение было основным источником питания для большинства травоядных динозавров? 🌿", "answers": ["a) Папоротник", "b) Цветок", "c) Кустарник", "d) Хвоя"], "correct": "a) Папоротник"},
    {"question": "Какая теория объясняет исчезновение динозавров? 💥", "answers": ["a) Атомная война", "b) Пандемия", "c) Астероидный удар", "d) Изменение климата"], "correct": "c) Астероидный удар"},
    {"question": "Какой динозавр был первым открытым учеными? 🦕", "answers": ["a) Брахиозавр", "b) Тираннозавр Рекс", "c) Стегозавр", "d) Мегалозавр"], "correct": "d) Мегалозавр"},
    {"question": "Какой динозавр имел гребень на своей голове? 🦚", "answers": ["a) Трицератопс", "b) Анкилозавр", "c) Паразавролоф", "d) Диплодок"], "correct": "c) Паразавролоф"},
    {"question": "Какой динозавр имел самый длинный шею? 🦕", "answers": ["a) Апатозавр", "b) Брахиозавр", "c) Маменхизавр", "d) Дилофозавр"], "correct": "c) Маменхизавр"},
    {"question": "Какой динозавр был назван в честь великого британского палеонтолога? 🦖", "answers": ["a) Дарвинозавр", "b) Ньютонозавр", "c) Хитчкокозавр", "d) Оуэнодон"], "correct": "d) Оуэнодон"},
    {"question": "Какая группа динозавров включала большинство хищников? 🦕", "answers": ["a) Сауроподы", "b) Тероподы", "c) Завроподы", "d) Анкилозавры"], "correct": "b) Тероподы"},
    {"question": "Какой динозавр считается самым быстрым на ногах? 🏃‍♂️", "answers": ["a) Трицератопс", "b) Брахиозавр", "c) Велоцираптор", "d) Стегозавр"], "correct": "c) Велоцираптор"},
    {"question": "Какой динозавр считается предком птиц? 🐦", "answers": ["a) Археоптерикс", "b) Птеранодон", "c) Компсогнат", "d) Микрораптор"], "correct": "a) Археоптерикс"},
    {"question": "Какой динозавр был одним из первых обнаруженных с перьями? 🦖", "answers": ["a) Тираннозавр Рекс", "b) Трицератопс", "c) Велоцираптор", "d) Синозавроптерикс"], "correct": "d) Синозавроптерикс"},
    {"question": "Какой динозавр был одним из немногих, способных плавать? 🌊", "answers": ["a) Брахиозавр", "b) Спинозавр", "c) Стегозавр", "d) Аллозавр"], "correct": "b) Спинозавр"},
    {"question": "Какой динозавр считается 'королем хищников'? 👑", "answers": ["a) Спинозавр", "b) Велоцираптор", "c) Тираннозавр Рекс", "d) Аллозавр"], "correct": "c) Тираннозавр Рекс"},
    {"question": "Какой динозавр обладал острыми рогоподобными структурами на хвосте для защиты? 🦏", "answers": ["a) Стегозавр", "b) Трицератопс", "c) Анкилозавр", "d) Брахиозавр"], "correct": "c) Анкилозавр"},
    {"question": "Какой динозавр считается самым умным? 🧠", "answers": ["a) Пахицефалозавр", "b) Паразавролоф", "c) Стегозавр", "d) Велоцираптор"], "correct": "d) Велоцираптор"},
    {"question": "Какой динозавр был назван в честь олимпийского богатыря? 🏛️", "answers": ["a) Гераклезавр", "b) Зевсозавр", "c) Аполлозавр", "d) Афродон"], "correct": "a) Гераклезавр"},
    {"question": "Какой динозавр был первым, открытым на территории современной России? 🇷🇺", "answers": ["a) Амурозавр", "b) Сиберотитан", "c) Мозазавр", "d) Оренбургозавр"], "correct": "a) Амурозавр"},
]


current_question = 0  # Индекс текущего вопроса


# Функция для отправки текущего вопроса и удаления предыдущего вопроса
def send_question(chat_id):
    global prev_question_message_id

    if prev_question_message_id:
        bot.delete_message(chat_id, prev_question_message_id)  # Удаляем предыдущий вопрос

    question_data = questions[current_question]
    keyboard = types.InlineKeyboardMarkup()
    for i, answer in enumerate(question_data["answers"]):
        button = types.InlineKeyboardButton(answer, callback_data=f"{current_question}-{i}")
        keyboard.add(button)

    message = bot.send_message(chat_id, question_data["question"], reply_markup=keyboard)
    prev_question_message_id = message.message_id


# Id администратора (замените на ваш id, который вы получили после отправки /start)
admin_id = 1281869576


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    global good  # Сбросим счетчик правильных ответов при новой викторине
    global user_info
    global q
    global current_question
    global prev_question_message_id

    good = 0
    user = message.from_user
    if user.username:
        user_info = user.username
    else:
        user_info = f"id: {user.id}"

    if user_info not in q:
        bot.send_photo(message.chat.id, "https://lh3.googleusercontent.com/pw/AIL4fc_z_PJBJINOIO3JDs-V9NE1phN9UYMGhuxGKGOeBQOZ7vQ-DPXuZ9CG5hP_spnA8oJqXAA9ip9NnZYsCgWdESUPwf_C2WvkFQ77O4hSqmVKc3K_JvbFR-HfNgsx5PEXtl2duMgXA2IZsK9MV4EJPSGLQ9JCkp6RPLQEliywRdQsHcGD4gyzPqfuWnL1pOgVBBydqON2ApPsx1UyPN8ESSZJhqKCBvmz3j-FJT0OG4mOadFfw5XO0vVGRIic_QjBAJE44r4yEsgKxVhHqrO1BiwbDBhTAFMeHS2t5Ja2_-MywF7MRVwAIJdRVpAu9YR9sMnJKYk7RSTXgZphQuEAxLdkZIfdvtQQCBBUj_UijoikfQltTJ4nr17H7Y4uMemwc8Wat-iwsME_IUFcE_ODgLu4G9aRinEZL-PzCUB0_21vzCoG3U3_8htAcPFmQ9RDNtcwYDyM5vi6PuGdN558RghKyf0WHxnWWdJYuwN41Lc7HXaMyYWG0vx_TaqiQx5NKEGJZtj4sgqeAg8J8Y2FvrbmGFZlUENswuvlYiAkOleC52GyjXbnimBvrbtPBWW81bP7_dLwuvPplfwK9ekBTQqPSHWAwruBMR9CjURmm8gYj0px3VvDNfSnC_mBPDZdIh0Cjal6bmXI0J3M1YOu6nOi4a7YJ4H4mdLXDZQWepdAz_eWKJ4v13tHkIR5VrgsrZKDdDpLa9cdlFD-W1keEKpAlRZsDNX31JL3digaRszSJ_sNdhzi3tAikfEY5v9cZmgdDDtSE8S1mxOV-vDOIB1v4kyDfmvUh7tf6N58Y42OkgGSITg4YAU-EuZC58UY7IXi78fDsZiL5keC-6KCjf4HM2oKGzuH_tbYhcfuoL0HOTtUClSX2irdnSDOZIsubMkWqye9CuKfX76QDNdyjA=w1080-h1080-s-no?authuser=0")
        bot.send_message(message.chat.id, "Здравствуй! Вы сейчас будете проходить Quiz от Mintodinos.\nВсего будет 20 вопросов")
        send_question(message.chat.id)
    else:
        bot.send_message(message.chat.id, "Ты уже проходил квиз, обмануть не получиться 😡")


# Обработчик нажатий на кнопки inline клавиатуры
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global current_question
    global good
    global user_info
    global q

    question_data = questions[current_question]
    question_index, answer_index = call.data.split('-')
    question_index = int(question_index)
    answer_index = int(answer_index)
    if question_index == current_question:
        selected_answer = question_data["answers"][answer_index]
        correct_answer = question_data["correct"]
        if selected_answer == correct_answer:
            good += 1

        current_question += 1  # Переходим к следующему вопросу

        if current_question < len(questions):
            send_question(call.message.chat.id)
        else:
            bot.send_message(call.message.chat.id, "Конец викторины! Спасибо за участие.😊")
            q.append(user_info)

            # Отправляем результаты администратору
            result_message = f"{user_info} - {good}"
            bot.send_message(admin_id, result_message)  # Отправляем результаты только администратору

            # Сбрасываем счетчик вопросов и очищаем предыдущий вопрос
            current_question = 0
            good = 0
            global prev_question_message_id
            prev_question_message_id = None


bot.polling(none_stop=True)
