import tweepy
from tweepy import OAuthHandler

exclude_words = ['el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'al', 'del', 'lo', 'le', 'y', 'e', 'o', 'u', 'de', 'a', 'en', 'que', 'es', 'por', 'para', 'con', 'se', 'su', 'les', 'me', 'q', 'te', 'pero', 'mi', 'ya', 'cuando', 'como', 'estoy', 'voy', 'porque', 'he', 'son', 'solo', 'tengo', 'muy']
API_KEY = 'DiHteES2UsuwBm4N68CfMZXta'
API_SECRET_KEY = '89qkZdkt66WxYCAm9FmAf0YEuHryA8WUWNr3ymaP8pD1j7llo3'
ACCESS_TOKEN = '859889173255389186-6WzryMui0Eid9Pmb6FOxPyrueyoqcgo'
ACCESS_TOKEN_SECRET = 'U43weqUi4V5dRUmOgnJipFWE6m4KZ8jeuMT6aB1yUCvWM'

def abrir_digitos(a):
    f = open(a+'.txt', 'r', encoding='utf-8')
    dato = f.read()
    print(dato)
    f.close
    #for linea in f.readlines():
    #    print(linea)
    

if __name__ == '__main__':
    tema = str(input('Que quieres saber?'))
    Opcion = int(input('Que deseas?'))
    if Opcion == 2:
        abrir_digitos(tema)

    if Opcion == 1:
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)

        public_tweets = api.home_timeline()
    #for tweet in public_tweets:
    #    print(f'{tweet.user.screen_name}:\n{tweet.text}\n{"*"*60}')
        id = None
        count = 0
        while count <= 3000:
            tweets = api.search(q=tema, lang='es', tweet_mode='extended', max_id=id)
            for tweet in tweets:
                f = open('./'+tema+'.txt', 'a', encoding='utf-8')
                f.write(tweet.full_text + '\n')
                f.close
            id = tweet.id

