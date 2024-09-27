from .models import Post

class PostRepository:
    @staticmethod
    def get_all_posts():
        return Post.objects.all()

    @staticmethod
    def get_post_by_id(post_id):
        return Post.objects.get(id=post_id)

    @staticmethod
    def create_post(data):
        post = Post(**data)
        post.save()
        return post

    @staticmethod
    def update_post(post_id, data):
        post = Post.objects.get(id=post_id)
        for key, value in data.items():
            setattr(post, key, value)
        post.save()
        return post

    @staticmethod
    def delete_post(post_id):
        post = Post.objects.get(id=post_id)
        post.delete()