from twilio.rest import Client
from secrets import sid, token, trial_number, my_number

client = Client(sid, token)


def call_me():

    try:
        client.calls.create(url='http://demo.twilio.com/docs/voice.xml',
                            to=my_number,
                            from_=trial_number)

        print('Called you!')
    except Exception:
        print('Failed to call...')


def text_me(message_body):

    try:
        client.messages.create(body=message_body,
                               from_=trial_number,
                               to=my_number)

        print('Sent you a text message!')
    except Exception:
        print(f'Failed to text the following:\n{message_body}')


if __name__ == '__main__':
    pass
