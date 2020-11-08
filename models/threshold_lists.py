from models import db, Node_Base, Column, relationship
class Threshold_list(Node_Base):
    __tablename__ = 'threshold_lists'
    id=Column(db.Integer,primary_key=True,autoincrement=True)
    description=Column(db.String(255))
    thresholdobjects=relationship("Thresholdobject",  back_populates="threshold_list")
    polldatatemplate=relationship("Polldatatemplate", back_populates="threshold_list")
    polleddatas=relationship("Polleddata",  back_populates="threshold_list")
    def __repr__(self):
        return "<Threshold_list(id='%s',description='%s')>" %(self.id,self.description)