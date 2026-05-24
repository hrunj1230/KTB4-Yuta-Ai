from sqlalchemy import Column, Integer, String
from db.database import Base

class Board(Base):
    __tablename__ = "boards"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer)
    def to_dict(self):
        return{
            "id": self.id,
            "title":self.title,
            "content":self.content,
            "user_id":self.user_id
        }