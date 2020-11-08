from models import db, Node_Base, Column, relationship,generate_uuid
class Alert(Node_Base):
    __tablename__ = 'alert'
    alertid=Column(db.String(255),primary_key=True,default=generate_uuid)          
    alarmRaisedTime=Column(db.BigInteger)
    alarmChangedTime=Column(db.BigInteger)
    alarmClearedTime=Column(db.BigInteger)
    state=Column(db.String(45))
    perceivedSeverity=Column(db.String(45))
    eventTime=Column(db.Integer)
    eventType=Column(db.String(255))
    faultType=Column(db.String(255))
    probableCause=Column(db.String(255))
    isRootCause=Column(db.Integer)
    correlatedAlarmId=Column(db.Integer)
    faultDetails=Column(db.String(255))
    deviceid=Column(db.Integer , db.ForeignKey('devicedetails.did'))
    metricid=Column(db.Integer , db.ForeignKey('metricdetails.metricid'))

    devicedetail=relationship("Devicedetail")
    metricdetail=relationship("Metricdetail")


    #
    def __repr__(self):
        return "<Alert(alertid='%s',alarmRaisedTime='%s',alarmChangedTime='%s',alarmClearedTime='%s',state='%s',perceivedSeverity='%s',eventTime='%s',eventType='%s',faultType='%s',probableCause='%s',isRootCause='%s',correlatedAlarmId='%s',faultDetails='%s',deviceid='%s',metricid='%s')>" %(self.alertid,self.alarmRaisedTime,self.alarmChangedTime,self.alarmClearedTime,self.state,self.perceivedSeverity,self.eventTime,self.eventType,self.faultType,self.probableCause,self.isRootCause,self.correlatedAlarmId,self.faultDetails,self.deviceid,self.metricid)