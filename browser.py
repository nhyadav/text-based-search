import sys
import os
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore
init()

args = sys.argv
directory = args[1]

if not os.path.exists(directory):
    os.makedirs(directory)
# write your code here
stack = deque()
while True:
    url = input()
    if url == 'exit':
        break
    elif url == 'back':
        stack.pop()
        with open(directory+'/'+str(stack[-1]), 'r') as data:
            text = data.read()
        print(text)
    else:
        prefix = 'https://'
        full_url = prefix + url
        try:
            r = requests.get(full_url)
            soup = BeautifulSoup(r.content, 'html.parser')
            tags = soup.find_all(['a','p','li'])
            filename = url.rstrip('.')
            with open(directory + '/' + str(filename), 'a', encoding='utf-8') as data :
                for tag in tags:
                    if tag.name == 'a':
                        print(Fore.BLUE + tag.text, file=data)
                    else:
                        print(tag.text, file=data)
            stack.append(filename)
            with open(directory + '/' + str(filename), 'r', encoding='utf-8') as data :
                text = data.read()
            print(text)
        except requests.exceptions.ConnectionError:
            print('Incorrect URL')















        # if url == 'bloomberg.com':
        #     with open(directory + '/' + str(url.split('.')[0]), 'a') as data:
        #         data.write(bloomberg_com)
        #     stack.append(url)
        #     print(bloomberg_com)
        # elif url == 'nytimes.com':
        #     with open(directory + '/' + str(url.split('.')[0]), 'a') as data:
        #         data.write(nytimes_com)
        #     stack.append(url)
        #     print(nytimes_com)
        # else:
        #     try:
        #         with open(directory + '/' + str(url), 'r') as data:
        #             url_data = data.read()
        #         print(url_data)
        #
        #     except Exception as exp:
        #         print("Error: Incorrect URL")


