import movieDatabaseServices as services

def getService(text, botName):
    botInstance = '#' + botName + ':'

    imdb = text.find(botInstance + 'imdb')
    help = text.find(botInstance + 'help')

    if imdb != -1 and help != -1:
        return 'error'
    if imdb != -1:
        return 'imdb'
    if help != -1:
        return 'help'

def startService(tweet, api, service):
    result = ''
    if service == 'imdb':
        result = services.imdbService(tweet, api)
    if service == 'help':
        result = services.helpService(tweet, api)
    if service == 'error':
        result = 'Error: Invalid service!'
    return result