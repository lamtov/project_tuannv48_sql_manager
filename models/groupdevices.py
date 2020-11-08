from models import db, Node_Base, Column, relationship
class Groupdevice(Node_Base):
    __tablename__ = 'groupdevices'
    group_id=Column(db.Integer,primary_key=True,autoincrement=True)
    group_name=Column(db.String(255)) 
    group_desc=Column(db.Text)
    is_manual=Column(db.Integer)         
    #
    groupdevicesdevicedetails=relationship("Groupdevicesdevicedetail",  back_populates="groupdevice")
    polleddatas=relationship("Polleddata",  back_populates="groupdevice")
    groupdevicepolledatatemplates=relationship("Groupevicepolledatatemplate",  back_populates="groupdevice")

    def __repr__(self):
        return "<Groupdevice(group_id='%s',group_name='%s',group_desc='%s',is_manual='%s')>" %(self.group_id,self.group_name,self.group_desc,self.is_manual)