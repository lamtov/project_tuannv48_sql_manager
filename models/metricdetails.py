from models import db, Node_Base, Column, relationship
class Metricdetail(Node_Base):
    __tablename__ = 'metricdetails'
         
    metricid=Column(db.Integer,primary_key=True,autoincrement=True)
    metricname=Column(db.Text)  
    description=Column(db.Text) 
    displayname=Column(db.Text) 
    metrictype=Column(db.Integer)   
    datatype=Column(db.String(255))    

    protocolid=Column(db.Integer , db.ForeignKey('protocoldetails.protocolid')) 
    protocoldetail=relationship("Protocoldetail")

    alerts = relationship("Alert", back_populates="metricdetail")
    polldatatemplate=relationship("Polldatatemplate", back_populates="metricdetail")
    polleddatas=relationship("Polleddata",  back_populates="metricdetail")
    def __repr__(self):
        return "<Metricdetail(metricid='%s',metricname='%s',description='%s',displayname='%s',metrictype='%s',datatype='%s',protocolid='%s')>" %(self.metricid,self.metricname,self.description,self.displayname,self.metrictype,self.datatype,self.protocolid)