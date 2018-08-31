from elasticsearch_dsl import Q


from datetime import timedelta

class ArticleQueryBuilder():
    def __init__(self, article):
        self.article = article

        
    def simple_and_query(self):
        return Q("match", title=self.article.title) & Q("match", body=self.article.text)
        
        
    def simple_or_query(self):
        return Q("match", title=self.article.title) | Q("match", body=self.article.text)
    
    
    def date_filter(self, before=timedelta(weeks=2),
                            after=timedelta(weeks=8)):
        date = self.article.publish_date.date()
        return Q("bool", filter=[Q('range', 
                            published={
                                'gte': date - before,
                                'lte': date + after
                            })])
    
    def location_query(self, locations):
        return Q("bool", should=[
            Q("match", body=locations), 
            Q("match", title=locations),
            Q("match", officeName=locations)])