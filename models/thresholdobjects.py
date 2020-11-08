from models import db, Node_Base, Column, relationship
class Thresholdobject(Node_Base):
    __tablename__ = 'thresholdobjects'
    id=Column(db.Integer,primary_key=True,autoincrement=True)
    name=Column(db.String(255))               
    kind=Column(db.String(255))               
    priority=Column(db.Integer)            
    category=Column(db.String(255))           
    thresholdvalue=Column(db.Integer)      
    rearmvalue=Column(db.Integer)          
    mmessage=Column(db.String(255))           
    allowed=Column(db.Integer)             
    is_customize=Column(db.Integer)        
    consecutive_time=Column(db.Integer)    
      
    operator=Column(db.String(45))
    severity=Column(db.String(45))   
    threshold_lists_id=Column(db.Integer , db.ForeignKey('threshold_lists.id'))
    threshold_list = relationship("Threshold_list")
    def __repr__(self):
        return "<Thresholdobject(id='%s',name='%s',kind='%s',priority='%s',category='%s',thresholdvalue='%s',rearmvalue='%s',mmessage='%s',allowed='%s',is_customize='%s',consecutive_time='%s',operator='%s',severity='%s',threshold_lists_id='%s')>" %(self.id,self.name,self.kind,self.priority,self.category,self.thresholdvalue,self.rearmvalue,self.mmessage,self.allowed,self.is_customize,self.consecutive_time,self.operator,self.severity, self.threshold_lists_id)