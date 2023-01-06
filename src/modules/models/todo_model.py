from sqlalchemy import Boolean, Column, Integer, String

from ...database import Base


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(Boolean, default=False)

    def as_dict(self):
        return {"id": self.id, "title": self.title, "completed": self.completed}
