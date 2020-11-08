from models import db, Node_Base, Column, relationship
class Groupalert(Node_Base):
    __tablename__ = 'groupalerts'
    group_id=Column(db.Integer,primary_key=True,autoincrement=True)
    group_name=Column(db.String(255))
    group_desc=Column(db.Text)


    def __repr__(self):
        return "<Groupalert(group_id='%s',group_name='%s',group_desc='%s')>" %(self.group_id,self.group_name,self.group_desc)