from .repositories import PostDatabaseRepo, PostCacheRepo 
from .unit_repositories import PostRepo
from .interactors import GetPostInteractor


class PostDatabaseRepoFactory(object):
    @staticmethod 
    def get():
        return PostDatabaseRepo()


class PostCacheRepoFactory(object):
    @staticmethod 
    def get():
        return PostCacheRepo()


class PostRepoFactory(object): 
    @staticmethod
    def get():
        db_repo = PostDatabaseRepoFactory.get() 
        cache_repo = PostCacheRepoFactory.get()
        return PostRepo(db_repo, cache_repo)


class GetPostInteractorFactory(object):
    @staticmethod 
    def get():
        product_repo = PostRepoFactory.get() 
        return GetPostInteractor(product_repo)


class PostViewFactory(object):
    @staticmethod 
    def create():
        get_product_interactor = GetPostInteractorFactory.get() 
        return PostView(get_product_interactor)
