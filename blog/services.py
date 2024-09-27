from .repositories import PostRepository

class PostService:
    @staticmethod
    def get_posts():
        return PostRepository.get_all_posts()

    @staticmethod
    def get_post(post_id):
        return PostRepository.get_post_by_id(post_id)

    @staticmethod
    def create_post(data):
        return PostRepository.create_post(data)

    @staticmethod
    def update_post(post_id, data):
        return PostRepository.update_post(post_id, data)

    @staticmethod
    def delete_post(post_id):
        return PostRepository.delete_post(post_id)