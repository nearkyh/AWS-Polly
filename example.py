from boto3 import client

def aws_polly_tts():
    polly = client('polly', region_name='us-west-2')

    response = polly.synthesize_speech(
            Text=input_msg,
            OutputFormat='mp3',
            VoiceId=name_id)

    stream = response.get('AudioStream')

    with open('output_aws_polly.mp3', 'wb') as f:
        data = stream.read()
        f.write(data)

input_msg = input('msg >> ')
name_id = 'Seoyeon'

aws_polly_tts()
