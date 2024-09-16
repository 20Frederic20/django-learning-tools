class Post(object):
    def __init__(self, uuid, slug, title, body, author, publish, status):
        self._uuid = uuid
        self._slug = slug
        self._title = title
        self._body = body
        self._author = author
        self._publish = publish
        self._status = status

    @property
    def uuid(self):
        return self._uuid

    @property
    def slug(self):
        return self._slug

    @property
    def title(self):
        return self._title

    @property
    def body(self):
        return self._body

    @property
    def author(self):
        return self._author

    @property
    def publish(self):
        return self._publish

    @property
    def status(self):
        return self._status