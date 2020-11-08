from models import db, Node_Base, Column, relationship
class Protocoldetail(Node_Base):
    __tablename__ = 'protocoldetails'
    protocolid=Column(db.Integer,primary_key=True,autoincrement=True)
    protocolname=Column(db.String(255))



    metricdetails=relationship("Metricdetail",  back_populates="protocoldetail")

    def __repr__(self):
        return "<Protocoldetail(protocolid='%s',protocolname='%s')>" %(self.protocolid,self.protocolname)