import datetime
from haystack import indexes
from home.models import Post , Note


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    first_name  = indexes.CharField(document=True, use_template=True)
    #author = indexes.CharField(model_attr='user')
    #second_name = indexes.CharField(model_attr='second_name')
    #phone_number = indexes.IntegerField(model_attr='phone_number')
    #file_number = indexes.IntegerField(model_attr='file_number')
    #age = indexes.IntegerField(model_attr='age')
    #id_number = indexes.IntegerField(model_attr='id_number')
    #patient_category = indexes.CharField(model_attr='patient_category')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Note

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())