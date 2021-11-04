# Using the requests and time modules, create a function which returns the amount of time
#  it takes a webpage to load (how long it takes for a complete response to a request).
# Test your code with multiple sites such as google, ynet, imdb, etc.

from time import time
import requests


#this func measures how much a website takes to load
#it uses requests and time modules

def  measure_website_load_time(url, open = False):
    before = time()
    response = requests.get(url)
    if open:
        open_response_html_as_temp_file_on_pc(response.text)
    after = time()
    return f"The time it took for {url} to load was:\n{after-before:.3f} seconds"



def main():
    websites_urls = [
        'https://www.ynet.co.il',
        'https://www.google.co.il',
        'https://www.google.com',
        'https://www.imdb.com'
        ]

    #opening only ynet as html file on the pc
    # [print(measure_website_load_time(website,True if 'imdb' in website else False)) for website in websites_urls]

    #printing every side load time
    [print(measure_website_load_time(website)) for website in websites_urls]



import tempfile
import webbrowser
# just playing; this will receive the response text and open the html from it on the browser at your pc
def open_response_html_as_temp_file_on_pc(responseText):
    html = f'<html> {responseText}</html>'
    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html', encoding='utf-8') as f:
            url = 'file://' + f.name
            f.write(html)
    webbrowser.open(url)



if __name__ == '__main__':
   main()


#Notes

#time.sleep(2) -> wait 2 seconds

#time.gmtime(0) for system's epoch

#time.time() for seconds since epoch

#time.time_ns(), time since epoch but in nanoseconds

#time.ctime() for current time as a string  -> Thu Nov  4 14:31:35 2021 - DAY MONTH DAYOFMONTH HOUR:MINUTE:SECOND YEAR
#or give it a time() inside -> t = time then ctime(t) -> string of that t time
#If you don’t pass an argument, then ctime() uses the return value of time() by default.
#the timestamp returned by ctime() depends on your geographical location. -> modifiable on the pc settings
#  Since local time is related to your locale, timestamps often account for locale-specific details such as the order of the elements in
#  the string and translations of the day and month abbreviations.
#  ctime() ignores these details.
# The representation of time dependent on your physical location is called local time and makes use of a concept called time zones.