import re
import pandas as pd

f = open('WhatsApp Chat with Viraj Kunjir IT C2.txt', 'r', encoding='UTF-8')

data = f.read()

print(data)

pattern = '\d{1,2}/\d{1,2}/\d{2},\s\d{1,2}:\d{2}\s-\s'

messages = re.split(pattern, data)[1:]
print(messages)

dates = re.findall(pattern, data)
print(dates)

df = pd.DataFrame({'user_message': messages, 'message_date': dates})
# convert message_date type
df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %H:%M - ')

df.rename(columns={'message_date': 'date'}, inplace=True)

df.head()

# Separate users and message
users = []
messages = []
for message in df['user_message']:
    entry = re.split('([\w\W]+?):\s', message)
    if entry[1:]: #user name
        users.append(entry[1])
        messages.append(entry[2])
    else:
        users.append('group_notification')
        messages.append(entry[0])

df['users'] = users
df['message'] = messages
# df['year'] = df['date'].dt.year
# df['month'] = df['date'].dt.month_name()
# df['day'] = df['date'].dt.day
# df['hours'] = df['date'].dt.hour
# df['minute'] = df['date'].dt.minute
df.drop(columns=['user_message'], inplace=True)

# df.head()
print(df)