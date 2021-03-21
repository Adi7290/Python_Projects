import pyshorteners

url = input('Enter your Url Plase:\t')
shortened = pyshorteners.Shortener()
print('-----Processing/')
print(f'Shortened url is :\t{shortened.tinyurl.short(url)}')