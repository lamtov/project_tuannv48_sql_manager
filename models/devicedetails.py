from models import db, Node_Base, Column, relationship
class Devicedetail(Node_Base):
    __tablename__ = 'devicedetails'
    did=Column(db.Integer,primary_key=True,autoincrement=True)
    mode=Column(db.String(255), default="")
    status=Column(db.Text)
    errorstring=Column(db.String(255))
    timeinterval=Column(db.String(255))
    last_updated_on=Column(db.DateTime)
    isprofilebased=Column(db.Integer)   
    fetch_rules=Column(db.Integer)      
    ip=Column(db.String(255))

    polleddatas=relationship("Polleddata",  back_populates="devicedetail")
    groupdevicesdevicedetails=relationship("Groupdevicesdevicedetail", uselist=False, back_populates="devicedetail")
    alerts = relationship("Alert",  back_populates="devicedetail")

    def __repr__(self):
        return "<Devicedetail(did='%s',mode='%s',status='%s',errorstring='%s',timeinterval='%s',last_updated_on='%s',isprofilebased='%s',fetch_rules='%s',ip='%s')>" %(self.did,self.mode,self.status,self.errorstring,self.timeinterval,self.last_updated_on,self.isprofilebased,self.fetch_rules,self.ip)