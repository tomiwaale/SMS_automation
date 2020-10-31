import random, schedule, time
import datetime

from twilio.rest import Client




GOOD_MORNING_QUOTES = [
    "Good Morning Love! Hope You Have An Amazing Day <3",
    "Good Morning Lovely! Hope you slept well <3",
    "Hope you have a great day today, my love!",
    "Love you so much, I know you will slay the day",
    "Good morning baby. I just wanted you to know how much I care for you. You’re always in my thoughts. Have an amazing day.",
    "Thank you so much for existing in my life, Love. I love you so much; Good Morning.",
    "Every morning I wake up knowing that you are mine and nothing makes me happier. May you have a merry and cheerful day, Beautiful.",
    "Thank you for making every morning such a great one, my darling. I love you to the moon and back. Good Morning, have a great day ahead.",
    "Good morning my love. A beautiful day is waiting outside just for you. Open your eyes and experience the excellence of nature around you.",
    "This wake-up text is for letting you know that you are the first thought on my mind every morning. I love you so much. Good morning!",
]

GOOD_EVENING_QUOTES = [
    "Good Evening Love",
    "Sleep Tight My Love!",
    "No matter how dark the night is, the moon of my life will always be shining with the light of a million stars. Good night my love!",
    "I’m so in love with you that I don’t know anymore when my nights end and when my days begin. Good night sweet dreams my love!",
    "Good night my love! I wish to be with you even in my dreams. Because you make them colorful for me!",
    "Goodnight sweetie, dream about the beauty of our relationship!",
    "Missing you more than I can express, thinking of you more than you know. Sleep well!",
    "I wish I was the pillow underneath your head or the blanket that warms your bed. I wish I was everything that you need at night!",
    "If I could list all the things I am grateful for today, you will be at the very top. Have a good night, my precious!",
    "Love you! I hope you dream about me tonight <3",
    "I am always comforted by the warmth of your love; I hope my affection reaches your heart too. Have a good night, dear!"
]









def send_message(quotes_list=None):
    now: int = datetime.datetime.now().hour
    if now < 10:
        quotes_list = GOOD_MORNING_QUOTES
    else:
        quotes_list = GOOD_EVENING_QUOTES

    account = "AC8cd6f128bcd5787ecf2984a44d1f1962"
    token = "a02b00e68b65ab2b144dd680b06374f8"
    client = Client(account, token)
    quote = quotes_list[random.randint(0, len(quotes_list)-1)]




    client.messages.create(to="+2347036911517",
                           from_='+12513519066',
                           body=quote
                           )


schedule.every().day.at("09:22").do(send_message)

schedule.every().day.at("21:31").do(send_message)









while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()

    time.sleep(2)

