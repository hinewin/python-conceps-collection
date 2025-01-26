#Create a class called Comment, attributes:
#username- username of user who created the comment
# text- The text/writing of the comment
# likes- numbers of likes the comment has. Always default to 0

class Comment:
    def __init__(self,username,text,likes=0):
        self.username = username
        self.text = text
        self.likes = likes
