from common.exceptions import EntityDoesNotExist 
from ..models import ORMPost
from .entities import Post

class PostRepo(object):
    def __init__(self, db_repo, cache_repo): 
        self.db_repo = db_repo 
        self.cache_repo = cache_repo

    def get_post(self, uuid):
        post = self.cache_repo.get_post(uuid)
        if post is None:
            post = self.db_repo.get_post(uuid) 
            self.cache_repo.save_post(post)
        return post


class PostDatabaseRepo(object):
    def get_product(self, uuid): 
        try:
            orm_product = ORMPost.objects.get(uuid=uuid)
        except ORMPost.DoesNotExist: 
            raise EntityDoesNotExist()
        return self._decode_orm_product(orm_product)

    def _decode_orm_product(self, orm_product):
        return Post(uuid=orm_product.uuid, slug=orm_product.slug, title=orm_product.title, body=orm_product.body, author=orm_product.author, publish=orm_product.publish, status=orm_product.status)
