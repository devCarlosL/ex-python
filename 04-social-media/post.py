from datetime import datetime
from random import randint

class User:
    def __init__(self, username, nickname) -> None:
        self.user_id = randint(0, 99999)
        self.username = username
        self.nickname = nickname

class Post(User):
    def __init__(self, user: User, message, comments = None) -> None:
        super().__init__(user.username, user.nickname)
        self.message = message
        self.post_datetime = datetime.now()

        if comments is None:
            self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)
    
    def get_comments(self):
        return self.comments

class Comment(User):
  def __init__(self, user: User, post: Post) -> None:
    super().__init__(user.username, user.nickname)
    self.post = post

  def create_comment(self, text: str):
    self.post.add_comment(text)
    self.comment_datetime = datetime.now()

print('--------------- Create User and Post ------------------')
user = User('Beltrano Lopes', 'beltranóis')
post = Post(user, 'Post 1')
post.add_comment('Comentário beltranóis')
print(f'{post.username} - {post.nickname} / {post.post_datetime}')
print(post.message)

print('---------------- Create Comment -----------------')
user2 = User('Fulano Silva', 'fulaninho')
comment = Comment(user2, post)
comment.create_comment('Comentário do fulaninho!')
print(f'{comment.username} - {comment.nickname} / {comment.comment_datetime}')

print('---------------- Post Comments -----------------')
post_comments = post.get_comments()
print(post_comments)