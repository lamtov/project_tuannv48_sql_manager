from models import  *


print("ok")

class AlertSchema(ma.ModelSchema):
    class Meta:
        model=Alert
class GroupevicepolledatatemplateSchema(ma.ModelSchema):
    class Meta:
        model=Groupevicepolledatatemplate

class DevicedetailsSchema(ma.ModelSchema):
    class Meta:
        model=Devicedetail

class GroupalertSchema(ma.ModelSchema):
    class Meta:
        model=Groupalert

# class GroupevicepolledatatemplateSchema(ma.ModelSchema):
#     class Meta:
#         model=Groupevicepolledatatemplate

class GroupdeviceSchema(ma.ModelSchema):
    class Meta:
        model=Groupdevice

class GroupdevicesdevicedetailSchema(ma.ModelSchema):
    class Meta:
        model=Groupdevicesdevicedetail

class MetricdetailSchema(ma.ModelSchema):
    class Meta:
        model=Metricdetail

class PolldatatemplateSchema(ma.ModelSchema):
    class Meta:
        model=Polldatatemplate

class PolleddataSchema(ma.ModelSchema):
    class Meta:
        model=Polleddata

class ProtocoldetailSchema(ma.ModelSchema):
    class Meta:
        model=Protocoldetail

class Threshold_listSchema(ma.ModelSchema):
    class Meta:
        model=Threshold_list

class ThresholdobjectSchema(ma.ModelSchema):
    class Meta:
        model=Thresholdobject




def to_json(querey_data, type_data, many):
    if type_data=='Alert':
        return AlertSchema(many=many).dump(querey_data).data
    elif  type_data=='Devicedetail':
        return DevicedetailsSchema(many=many).dump(querey_data).data
    elif  type_data=='Groupalert':
        return GroupalertSchema(many=many).dump(querey_data).data
    elif  type_data=='Groupevicepolledatatemplate':
        return GroupevicepolledatatemplateSchema(many=many).dump(querey_data).data
    elif  type_data=='Groupdevice':
        return GroupdeviceSchema(many=many).dump(querey_data).data
    elif  type_data=='Groupdevicesdevicedetail':
        return GroupdevicesdevicedetailSchema(many=many).dump(querey_data).data
    elif  type_data=='Metricdetail':
        return MetricdetailSchema(many=many).dump(querey_data).data
    elif  type_data=='Polldatatemplate':
        return PolldatatemplateSchema(many=many).dump(querey_data).data
    elif  type_data=='Polleddata':
        return PolleddataSchema(many=many).dump(querey_data).data
    elif  type_data=='Protocoldetail':
        return ProtocoldetailSchema(many=many).dump(querey_data).data
    elif  type_data=='Threshold_list':
        return Threshold_listSchema(many=many).dump(querey_data).data
    elif  type_data=='Thresholdobject':
        return ThresholdobjectSchema(many=many).dump(querey_data).data

    else:
        return {'ok': 'ok'}