from flask import Blueprint, abort, request
from sqlalchemy import or_
from .assets import *

from global_assets.custom_response import custom_response, custom_response_flask_restful
from flask_restplus import Api, Resource, Namespace, fields
import global_assets.const as CONST

namespace = Namespace(name='update', path='/', description='update data json to mysql')


@namespace.route('/update/update_alert', methods=['POST'])
class update_alert(Resource):
    resource_update_alert = namespace.model('update_alert',
                                         {'alertid':fields.String,'alarmRaisedTime': fields.String, 'alarmChangedTime': fields.String,
                                          'alarmClearedTime': fields.String, 'state': fields.String,
                                          'perceivedSeverity': fields.String, 'eventTime': fields.String,
                                          'eventType': fields.String, 'faultType': fields.String,
                                          'probableCause': fields.String, 'isRootCause': fields.String,
                                          'correlatedAlarmId': fields.String, 'faultDetails': fields.String,
                                          'deviceid': fields.String, 'metricid': fields.String})

    @namespace.doc(body=resource_update_alert)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json
        alert = session.query(models.Alert).filter_by(alertid=data.get('alertid')).first()
        if alert is None:
            return custom_response_flask_restful(request, 404, "alert chua ton tai", None, None)

        if data.get('alarmRaisedTime'): alert.alarmRaisedTime = data.get('alarmRaisedTime')
        if data.get('alarmChangedTime'): alert.alarmChangedTime = data.get('alarmChangedTime')
        if data.get('alarmClearedTime'): alert.alarmClearedTime = data.get('alarmClearedTime')
        if data.get('state'): alert.state = data.get('state')
        if data.get('perceivedSeverity'): alert.perceivedSeverity = data.get('perceivedSeverity')
        if data.get('eventTime'): alert.eventTime = data.get('eventTime')
        if data.get('eventType'): alert.eventType = data.get('eventType')
        if data.get('faultType'): alert.faultType = data.get('faultType')
        if data.get('probableCause'): alert.probableCause = data.get('probableCause')
        if data.get('isRootCause'): alert.isRootCause = data.get('isRootCause')
        if data.get('correlatedAlarmId'): alert.correlatedAlarmId = data.get('correlatedAlarmId')
        if data.get('faultDetails'): alert.faultDetails = data.get('faultDetails')
        if data.get('deviceid'): alert.deviceid = data.get('deviceid')
        if data.get('metricid') : alert.metricid = data.get('metricid')

        session.add(alert)
        session.commit()

        res = models.to_json(alert, 'Alert', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)


@namespace.route('/update/update_devicedetails', methods=['POST'])
class update_devicedetails(Resource):
    resource_update_devicedetails = namespace.model('update_devicedetails', {'did':fields.String,
        'mode': fields.String, 'status': fields.String, 'errorstring': fields.String, 'timeinterval': fields.String,
        'isprofilebased': fields.Integer, 'fetch_rules': fields.Integer, 'ip': fields.String
    })

    @namespace.doc(body=resource_update_devicedetails)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json

        device = session.query(models.Devicedetail).filter_by(did=data.get('did')).first()
        if device is None:
            return custom_response_flask_restful(request, 404, "device chua ton tai", None, None)

        if data.get('mode'): device.mode = data.get('mode')
        if data.get('status'): device.status = data.get('status')
        if data.get('errorstring'): device.errorstring = data.get('errorstring')
        if data.get('timeinterval'): device.timeinterval = data.get('timeinterval')
        device.last_updated_on = datetime.now()
        if data.get('isprofilebased'): device.isprofilebased = data.get('isprofilebased')
        if data.get('fetch_rules'): device.fetch_rules = data.get('fetch_rules')
        if data.get('ip'): device.ip = data.get('ip')

        session.add(device)
        session.commit()

        res = models.to_json(device, 'Devicedetail', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)


@namespace.route('/update/update_groupalerts', methods=['POST'])
class update_groupalerts(Resource):
    resource_update_groupalerts = namespace.model('update_groupalerts', {'group_id':fields.String,
        'group_name': fields.String, 'group_desc': fields.String
    })

    @namespace.doc(body=resource_update_groupalerts)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json

        groupalert = session.query(models.Groupalert).filter_by(group_id=data.get('group_id')).first()
        if groupalert is None:
            return custom_response_flask_restful(request, 404, "groupalert chua ton tai", None, None)

        if data.get('group_name'): groupalert.group_name = data.get('group_name')
        if data.get('group_desc'): groupalert.group_desc = data.get('group_desc')

        session.add(groupalert)
        session.commit()

        res = models.to_json(groupalert, 'Groupalert', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)


@namespace.route('/update/update_groupdevicepolledatatemplate', methods=['POST'])
class update_groupdevicepolledatatemplate(Resource):
    resource_update_groupdevicepolledatatemplate = namespace.model('update_groupdevicepolledatatemplate',
                                                                {'id':fields.String,'groupdevices_group_id': fields.String,
                                                                 'polldatatemplate_id': fields.String})

    @namespace.doc(body=resource_update_groupdevicepolledatatemplate)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json
        groupdevicesdevicedetail = session.query(models.Groupdevicesdevicedetail).filter_by(id=data.get('id')).first()
        if groupdevicesdevicedetail is None:
            return custom_response_flask_restful(request, 404, "groupdevicesdevicedetail chua ton tai", None, None)

        if data.get('devicedetail_did'): groupdevicesdevicedetail.devicedetail_did = data.get('devicedetail_did')

        if data.get('groupdevice_id'): groupdevicesdevicedetail.groupdevice_id = data.get('groupdevice_id')

        session.add(groupdevicepolledatatemplate)
        session.commit()

        res = models.to_json(groupdevicepolledatatemplate, 'Groupevicepolledatatemplate', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)


@namespace.route('/update/update_groupdevices', methods=['POST'])
class update_groupdevices(Resource):
    resource_update_groupdevices = namespace.model('update_groupdevices',
                                                {'group_id':fields.String,'group_name': fields.String, 'group_desc': fields.String,
                                                 'is_manual': fields.String})

    @namespace.doc(body=resource_update_groupdevices)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json
        groupdevice = session.query(models.Groupdevice).filter_by(group_id=data.get('group_id')).first()
        if groupdevice is None:
            return custom_response_flask_restful(request, 404, "groupdevice chua ton tai", None, None)
        if data.get('group_name'): groupdevice.group_name = data.get('group_name')
        if data.get('group_desc'): groupdevice.group_desc = data.get('group_desc')
        if data.get('is_manual'): groupdevice.is_manual = data.get('is_manual')

        session.add(groupdevice)
        session.commit()

        res = models.to_json(groupdevice, 'Groupdevice', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)


@namespace.route('/update/update_groupdevicesdevicedetails', methods=['POST'])
class update_groupdevicesdevicedetails(Resource):
    resource_update_groupdevicesdevicedetails = namespace.model('update_groupdevicesdevicedetails',
                                                             {'id':fields.String,'devicedetail_did': fields.String,
                                                              'groupdevice_id': fields.String})

    @namespace.doc(body=resource_update_groupdevicesdevicedetails)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json
        groupdevicesdevicedetail = session.query(models.Groupdevicesdevicedetail).filter_by(id=data.get('id')).first()
        if groupdevicesdevicedetail is None:
            return custom_response_flask_restful(request, 404, "groupdevicesdevicedetail chua ton tai", None, None)

        if data.get('devicedetail_did'): groupdevicesdevicedetail.devicedetail_did = data.get('devicedetail_did')
        if data.get('groupdevice_id'): groupdevicesdevicedetail.groupdevice_id = data.get('groupdevice_id')
        session.add(groupdevicesdevicedetail)
        session.commit()

        res = models.to_json(groupdevicesdevicedetail, 'Groupdevicesdevicedetail', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)


@namespace.route('/update/update_metricdetails', methods=['POST'])
class update_metricdetails(Resource):
    resource_update_metricdetails = namespace.model('update_metricdetails',
                                                 {'metricid':fields.String,'metricname': fields.String, 'description': fields.String,
                                                  'displayname': fields.String, 'metrictype': fields.String,
                                                  'datatype': fields.String, 'protocolid': fields.String})

    @namespace.doc(body=resource_update_metricdetails)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json
        metricdetails = session.query(models.Metricdetail).filter_by(metricid=data.get('metricid')).first()
        if metricdetails is None:
            return custom_response_flask_restful(request, 404, "metricdetails chua ton tai", None, None)
        protocoldetails = session.query(models.Protocoldetail).filter_by(protocolid=data.get('protocolid')).first()
        if protocoldetails is None:
            return custom_response_flask_restful(request, 404, "protocoldetails chua ton tai", None, None)

        if data.get('metricname'): metricdetails.metricname = data.get('metricname')
        if data.get('description'): metricdetails.description = data.get('description')
        if data.get('displayname'): metricdetails.displayname = data.get('displayname')
        if data.get('metrictype'): metricdetails.metrictype = data.get('metrictype')
        if data.get('datatype'): metricdetails.datatype = data.get('datatype')
        if data.get('protocolid'): metricdetails.protocolid = data.get('protocolid')

        session.add(metricdetails)
        session.commit()

        res = models.to_json(metricdetails, 'Metricdetail', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)


@namespace.route('/update/update_polldatatemplate', methods=['POST'])
class update_polldatatemplate(Resource):
    resource_update_polldatatemplate = namespace.model('update_polldatatemplate',
                                                    {'id':fields.String,'name': fields.String, 'agent': fields.String,
                                                     'period': fields.String, 'active': fields.String,
                                                     'oid': fields.String, 'threshold_activate': fields.String,
                                                     'protocol': fields.String, 'metricdetail_id': fields.String,
                                                     'threshold_list_id': fields.String})

    @namespace.doc(body=resource_update_polldatatemplate)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json
        polldatatemplate = session.query(models.Polldatatemplate).filter_by(id=data.get('id')).first()
        if polldatatemplate is None:
            return custom_response_flask_restful(request, 404, "polldatatemplate chua ton tai", None, None)
        if data.get('name'): polldatatemplate.name = data.get('name')
        if data.get('agent'): polldatatemplate.agent = data.get('agent')
        if data.get('period'): polldatatemplate.period = data.get('period')
        if data.get('active'): polldatatemplate.active = data.get('active')
        if data.get('oid'): polldatatemplate.oid = data.get('oid')
        if data.get('threshold_activate'): polldatatemplate.threshold_activate = data.get('threshold_activate')
        if data.get('protocol'): polldatatemplate.protocol = data.get('protocol')
        if data.get('metricdetail_id'): polldatatemplate.metricdetail_id = data.get('metricdetail_id')
        if data.get('threshold_list_id'): polldatatemplate.threshold_list_id = data.get('threshold_list_id')

        session.add(polldatatemplate)
        session.commit()

        res = models.to_json(polldatatemplate, 'Polldatatemplate', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)


@namespace.route('/update/update_polleddata', methods=['POST'])
class update_polleddata(Resource):
    resource_update_polleddata = namespace.model('update_polleddata',
                                              {'id':fields.String,'name': fields.String, 'agent': fields.String, 'period': fields.String,
                                               'active': fields.String, 'threshold_activate': fields.String,
                                               'devicedetails_did': fields.String,
                                               'groupdevices_group_id': fields.String,
                                               'threshold_lists_id': fields.String,
                                               'metricdetails_metricid': fields.String})

    @namespace.doc(body=resource_update_polleddata)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json
        polleddata = session.query(models.Polleddata).filter_by(id=data.get('id')).first()
        if polleddata is None:
            return custom_response_flask_restful(request, 404, "polleddata chua ton tai", None, None)

        if data.get('name'): polleddata.name = data.get('name')
        if data.get('agent'): polleddata.agent = data.get('agent')
        if data.get('period'): polleddata.period = data.get('period')
        if data.get('active'): polleddata.active = data.get('active')
        if data.get('threshold_activate'): polleddata.threshold_activate = data.get('threshold_activate')
        if data.get('devicedetails_did'): polleddata.devicedetails_did = data.get('devicedetails_did')
        if data.get('groupdevices_group_id'): polleddata.groupdevices_group_id = data.get('groupdevices_group_id')
        if data.get('threshold_lists_id'): polleddata.threshold_lists_id = data.get('threshold_lists_id')
        if data.get('metricdetails_metricid'): polleddata.metricdetails_metricid = data.get('metricdetails_metricid')

        session.add(polleddata)
        session.commit()

        res = models.to_json(polleddata, 'Polleddata', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)


@namespace.route('/update/update_protocoldetails', methods=['POST'])
class update_protocoldetails(Resource):
    resource_update_protocoldetails = namespace.model('update_protocoldetails', {'protocolid':fields.String,'protocolname': fields.String})

    @namespace.doc(body=resource_update_protocoldetails)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json

        protocoldetail = session.query(models.Protocoldetail).filter_by(protocolid=data.get('protocolid')).first()
        if protocoldetail is None:
            return custom_response_flask_restful(request, 404, "protocoldetail chua ton tai", None, None)
        if data.get('protocolname'): protocoldetail.protocolname = data.get('protocolname')

        session.add(protocoldetail)
        session.commit()

        res = models.to_json(protocoldetail, 'Protocoldetail', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)


@namespace.route('/update/update_threshold_lists', methods=['POST'])
class update_threshold_lists(Resource):
    resource_update_threshold_lists = namespace.model('update_threshold_lists', {'id':fields.String,'description': fields.String})

    @namespace.doc(body=resource_update_threshold_lists)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json
        threshold_list = session.query(models.Threshold_list).filter_by(id=data.get('id')).first()
        if threshold_list is None:
            return custom_response_flask_restful(request, 404, "threshold_list chua ton tai", None, None)

        if data.get('description'): threshold_list.description = data.get('description')

        session.add(threshold_list)
        session.commit()

        res = models.to_json(threshold_list, 'Threshold_list', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)


@namespace.route('/update/update_thresholdobjects', methods=['POST'])
class update_thresholdobjects(Resource):
    resource_update_thresholdobjects = namespace.model('update_thresholdobjects',
                                                    {'id':fields.String,'name': fields.String, 'kind': fields.String,
                                                     'priority': fields.String, 'category': fields.String,
                                                     'thresholdvalue': fields.String, 'rearmvalue': fields.String,
                                                     'mmessage': fields.String, 'allowed': fields.String,
                                                     'is_customize': fields.String, 'consecutive_time': fields.String,
                                                     'operator': fields.String, 'severity': fields.String, 'threshold_lists_id':fields.String})

    @namespace.doc(body=resource_update_thresholdobjects)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json
        thresholdobject = session.query(models.Thresholdobject).filter_by(id=data.get('id')).first()
        if thresholdobject is None:
            return custom_response_flask_restful(request, 404, "thresholdobject chua ton tai", None, None)

        if data.get('name'): thresholdobject.name = data.get('name')
        if data.get('kind'): thresholdobject.kind = data.get('kind')
        if data.get('priority'): thresholdobject.priority = data.get('priority')
        if data.get('category'): thresholdobject.category = data.get('category')
        if data.get('thresholdvalue'): thresholdobject.thresholdvalue = data.get('thresholdvalue')
        if data.get('rearmvalue'): thresholdobject.rearmvalue = data.get('rearmvalue')
        if data.get('mmessage'): thresholdobject.mmessage = data.get('mmessage')
        if data.get('allowed'): thresholdobject.allowed = data.get('allowed')
        if data.get('is_customize'): thresholdobject.is_customize = data.get('is_customize')
        if data.get('consecutive_time'): thresholdobject.consecutive_time = data.get('consecutive_time')
        if data.get('operator'): thresholdobject.operator = data.get('operator')
        if data.get('severity'): thresholdobject.severity = data.get('severity')
        if data.get('threshold_lists_id'): thresholdobject.threshold_lists_id = data.get('threshold_lists_id')

        session.add(thresholdobject)
        session.commit()

        res = models.to_json(thresholdobject, 'Thresholdobject', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)
