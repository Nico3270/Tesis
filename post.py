class User:
    def __init__ (self,name):
        self.name = name
        self.is_logged_in = False
        
def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(User):
    print(f"This is {User.name}' new blog post")
new_user = User("Nicolas")
new_user.is_logged_in = True
create_blog_post(new_user)
        

            
        
         