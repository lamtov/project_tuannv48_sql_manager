from models import db, Node_Base, Column, relationship
class Polleddata(Node_Base):
    __tablename__ = 'polleddata'
    id=Column(db.Integer,primary_key=True,autoincrement=True)
    name=Column(db.String(255))                   
    agent=Column(db.String(255))                  
    period=Column(db.Integer)                  
    active=Column(db.Integer)                  
    threshold_activate=Column(db.Integer)      
    devicedetails_did=Column(db.Integer , db.ForeignKey('devicedetails.did'))
    groupdevices_group_id=Column(db.Integer , db.ForeignKey('groupdevices.group_id'))
    threshold_lists_id=Column(db.Integer , db.ForeignKey('threshold_lists.id'))
    metricdetails_metricid=Column(db.Integer , db.ForeignKey('metricdetails.metricid'))

    devicedetail=relationship("Devicedetail")
    metricdetail=relationship("Metricdetail")
    threshold_list=relationship("Threshold_list")
    groupdevice=relationship("Groupdevice")

    def __repr__(self):
        return "<Polleddata(id='%s',name='%s',agent='%s',period='%s',active='%s',threshold_activate='%s',devicedetails_did='%s',groupdevices_group_id='%s',threshold_lists_id='%s',metricdetails_metricid='%s')>" %(self.id,self.name,self.agent,self.period,self.active,self.threshold_activate,self.devicedetails_did,self.groupdevices_group_id,self.threshold_lists_id,self.metricdetails_metricid)