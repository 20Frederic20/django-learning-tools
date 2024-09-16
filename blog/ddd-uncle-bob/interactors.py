class GetPostInteractor(object):
    def __init__(self, post_repo):
        self.post_repo = post_repo

    def set_params(self, uuid):
        self.uuid = uuid
        return self

    def execute(self):
        return self.post_repo.get_post(uuid=self.uuid)