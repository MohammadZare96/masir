from django_elasticsearch_dsl import DocType, Index
from models import *

# Name of the Elasticsearch index
masir = Index('masirs')
# See Elasticsearch Indices API reference for available settings
masir.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@masir.doc_type
class MasirDocument(DocType):
    class Meta:
        model = Masir # The model associated with this DocType

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'item_name',
            'new_price',
            'old_price',
            'discount_price',
            'discount_percent',
            'address',
            'item_image',
            'masir_cat',
            'brand',
            'time',
        ]

        # Ignore auto updating of Elasticsearch when a model is saved
        # or deleted:
        # ignore_signals = True
        # Don't perform an index refresh after every update (overrides global setting):
        # auto_refresh = False
        # Paginate the django queryset used to populate the index with the specified size
        # (by default there is no pagination)
        # queryset_pagination = 5000