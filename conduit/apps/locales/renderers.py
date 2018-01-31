
from conduit.apps.core.renderers import ConduitJSONRenderer


class LocalJSONRenderer(ConduitJSONRenderer):
    object_label = 'local'
    pagination_object_label = 'locales'
    pagination_count_label = 'localesCount'


class CommentJSONRenderer(ConduitJSONRenderer):
    object_label = 'comment'
    pagination_object_label = 'comments'
    pagination_count_label = 'commentsCount'


class ProductoJSONRenderer(ConduitJSONRenderer):
    object_label = 'producto'
    pagination_object_label = 'productos'
    pagination_count_label = 'productosCount'