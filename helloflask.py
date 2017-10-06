import sys
import os

from flask import Flask, request
sys.path.append(os.path.abspath("/Users/brandon/Webby/bagger/scripts"))
from handle_zip import url_grabber
sys.path.append(os.path.abspath("/Users/brandon/Webby/bagger/scripts/spiders"))
from spider_runners import start_spiders

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

# this tells flask what url should trigger this function
@app.route('/input')
def hello_world():
    zipcode = request.args.get('zipcode', 92122) # default zip = La Jolla
    recipe_url = request.args.get('recipe_link')
# url_grabber from handle_zip - requests the page that loads the weekly ad
    ad_url = url_grabber(zipcode)

    vonsurlfile = open('vonsurl', 'w')
    vonsurlfile.write(ad_url)
    vonsurlfile.close()

    recipesurlfile = open('allrecipes_url', 'w')
    recipesurlfile.write(recipe_url)
    recipesurlfile.close()


    start_spiders()
    
    return 'Parse this page! %s' % ad_url
# The function name is also used to generate URLs for the function 
