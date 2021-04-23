from flask import Flask
import requests
import os
import json

app = Flask(__name__)

# API_KEY = ""
API_KEY = os.environ['API_KEY']

@app.route('/')
def index():
    return 'App Works!'

@app.route('/<string:city>/<string:country>/')
def weather_by_city(country, city):

    # url = 'https://samples.openweathermap.org/data/2.5/weather'

    # api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=
    # url = 'https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID='
    url = 'https://api.openweathermap.org/data/2.5/weather'

    params = dict(
        q=city + "," + country,
        appid= API_KEY,
    )

    response = requests.get(url=url, params=params)
    data = response.json()
    return data

@app.route('/getfileinfo/<string:file_path>/')
def get_file_info(file_path):

    #    The longest word(s)
    #    Number of words
    #    Number of unique words
    #    Average word length
   
    longest_words = []
    number_of_words = 0
    number_of_unique_words = 0
    avg_word_lengh = 0

    max_len = 0 

    response = {}        
    #    with open(file_path) as reader:
    #       for line in reader:
    #         print(line, end='') 

    '''
    my_file = open(file_path, "r")
    # content = my_file.read()
    # print(content)

    # file_list = list(f)
    # file_list = content.split(",")

    file_list = my_file.readlines()
    my_file.close()
    print(file_list)
    '''

    file_list = []

    with open(file_path, "r") as f:
        for line in f:
            file_list.extend(line.split())

    print('file_list:', file_list)
    number_of_words = len(file_list)

    unique_set =  set(file_list)
    number_of_unique_words = len(unique_set)

    total_word_len = 0

    for word in file_list:
        word_len = len(word)
        total_word_len += word_len
        if word_len > max_len:
            max_len = word_len
            longest_words = []
            longest_words.append(word)

        elif word_len == max_len:
            longest_words.append(word)


    avg_word_lengh = int(total_word_len/number_of_words)

    response['longest_words'] = longest_words
    response['number_of_words'] = number_of_words
    response['number_of_unique_words'] = number_of_unique_words
    response['avg_word_lengh'] = avg_word_lengh

    # response = 'sample'
    # data = response.json()

    data = json.dumps(response)
    return data


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6000)



### TEST BLOCK ###
# file_path = 'sample_file.txt'

# print(get_file_info(file_path))
