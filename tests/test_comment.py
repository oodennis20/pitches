from app.models import Comments,User
from app import db

def tearDown(self):
        Review.query.delete()
        User.query.delete()

def test_save_comment(self):
        self.new_comment.save_review()
        self.assertTrue(len(Comment.query.all())>0)