class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = True

def is_authenticated_decorator(function):
    def wrapper(*args,**kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper
@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is a blog post in {user.name}'s blog")


new_user = User("Ricardo")
create_blog_post(new_user)
