from models import db, Node_Base, Column, relationship
class Groupdevicesdevicedetail(Node_Base):
    __tablename__ = 'groupdevicesdevicedetails'
    id=Column(db.Integer,primary_key=True,autoincrement=True)
    devicedetail_did=Column(db.Integer , db.ForeignKey('devicedetails.did'))
    groupdevice_id=Column(db.Integer , db.ForeignKey('groupdevices.group_id'))
    devicedetail=relationship("Devicedetail")
    groupdevice=relationship("Groupdevice")



    def __repr__(self):
        return "<Groupdevicesdevicedetail(id='%s',devicedetail_did='%s',groupdevice_id='%s')>" %(self.id,self.devicedetail_did,self.groupdevice_id)