import requests
import re
'''


'''
searchcard = input('what name are you searching for? ')

url3 = f'http://www.starcitygames.com/results?name={searchcard}&go.x=0&go.y=0&go=GO'

r3 = requests.get(url3)

with open('site_output.html','w') as output_file:
    output_file.write(r3.text)

with open('site_output.html','r') as output_file:
    contents = output_file.read()

with open('pricelist.txt','w') as price_data:
    price_data.write(str(re.findall('tooltip="([^\>]{,60})"[^$]{60}[^$]*(\$.{,5})',contents)))

x = re.findall('tooltip="([^\>]{,60})"[^$]{60}[^$]*(\$.{,5})',contents)

print(type(x[0]))