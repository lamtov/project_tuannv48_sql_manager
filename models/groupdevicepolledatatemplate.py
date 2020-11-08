from models import db, Node_Base, Column, relationship
class Groupevicepolledatatemplate(Node_Base):
    __tablename__ = 'groupdevicepolledatatemplate'
    id=Column(db.Integer,primary_key=True,autoincrement=True)
    groupdevices_group_id=Column(db.Integer , db.ForeignKey('groupdevices.group_id'))
    polldatatemplate_id=Column(db.Integer , db.ForeignKey('polldatatemplate.id'))
    #
    groupdevice=relationship("Groupdevice")
    polldatatemplate=relationship("Polldatatemplate")


    def __repr__(self):
        return "<Groupevicepolledatatemplate(id='%s',groupdevices_group_id='%s',polldatatemplate_id='%s',groupdevice='%s',polldatatemplate='%s')>" %(self.id,self.groupdevices_group_id,self.polldatatemplate_id, self.groupdevice, self.polldatatemplate)