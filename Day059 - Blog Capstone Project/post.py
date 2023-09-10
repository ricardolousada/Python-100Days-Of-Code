class Post:
    def __init__(self,post_id, title,subtitle,author, body,image_url,image_alt, date):
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.body = body
        self.image_url = image_url
        self.image_alt = image_alt
        self.date = date