class PostSerializer(object):
    @staticmethod
    def serialize(post):
        return {
            'uuid': post.uuid,
            'slug': post.slug, 
            'title': post.title,
            'body': post.body,
            'author': post.author,
            'status': post.status,
            'publish': post.publish,
        }
