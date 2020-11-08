from models import db, Node_Base, Column, relationship
class Polldatatemplate(Node_Base):
    __tablename__ = 'polldatatemplate'
    id=Column(db.Integer,primary_key=True,autoincrement=True)
    name=Column(db.String(255))               
    agent=Column(db.String(255))              
    period=Column(db.Integer)              
    active=Column(db.Integer)              
    oid=Column(db.String(255))                
    threshold_activate=Column(db.Integer)  
    protocol=Column(db.String(255))       

    metricdetail_id=Column(db.Integer , db.ForeignKey('metricdetails.metricid'))
    threshold_list_id=Column(db.Integer , db.ForeignKey('threshold_lists.id'))
    

    #
    metricdetail=relationship("Metricdetail")
    threshold_list=relationship("Threshold_list")
    def __repr__(self):
        return "<Polldatatemplate(id='%s',name='%s',agent='%s',period='%s',active='%s',oid='%s',threshold_activate='%s',protocol='%s',metricdetail_id='%s',threshold_list_id='%s')>" %(self.id,self.name,self.agent,self.period,self.active,self.oid,self.threshold_activate,self.protocol,self.metricdetail_id,self.threshold_list_id)