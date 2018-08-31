import json

from flask import Flask, request, jsonify
from newspaper import Article
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
from flask_cors import CORS

import spacy

from query_builder import ArticleQueryBuilder

with open('backend/conf.json') as f:
    conf = json.load(f)

app = Flask(__name__)
CORS(app)

client = Elasticsearch(hosts=conf['host'], timeout=20)
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

@app.route('/', methods=['POST'])
def hello():
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
