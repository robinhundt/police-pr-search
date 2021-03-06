import json
import os

from flask import Flask, request, jsonify, render_template
from newspaper import Article
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
from flask_cors import CORS
from whitenoise import WhiteNoise

import spacy

from query_builder import ArticleQueryBuilder

elastic_host = os.environ['ELASTIC_HOST'] if \
            'ELASTIC_HOST' in os.environ else 'localhost'

app = Flask(__name__,
            static_folder="./frontend/dist/",
            template_folder="./frontend/dist")
app.wsgi_app = WhiteNoise(app.wsgi_app, root='frontend/dist')
CORS(app)


client = Elasticsearch(hosts=elastic_host, timeout=10)
nlp = spacy.load('de')

def transform_response(elastic_response):
    return [
        {
            'title': hit.title,
            'body': hit.body,
            'published': hit.published,
            'url': hit.URL,
            'score': hit.meta.score,
            'elastic_id': hit.meta.id,
            'id': hit.ID
        } for hit in elastic_response
    ]


def get_locations_from_article(article):
    doc = nlp(article.text)
    return " ".join([str(ent) for ent in doc.ents if ent.label_ == "LOC"])

@app.route('/api', methods=['POST'])
def api():
    req_data = request.get_json()
    url = req_data['url']
    article = Article(url=url, language='de')
    article.download()
    article.parse()

    locations = get_locations_from_article(article)

    q_builder = ArticleQueryBuilder(article)
    query = q_builder.simple_or_query()
    if article.publish_date is not None:
        query = query & q_builder.date_filter()

    if len(locations) > 0:
        query = query | q_builder.location_query(locations)
    
    search = Search(using=client)
    res = search.query(query).execute()

    return jsonify(transform_response(res))


@app.route('/')
def index():
    return render_template("index.html")
