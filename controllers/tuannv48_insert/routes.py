from flask import Blueprint, abort, request
from sqlalchemy import or_
from .assets import *

from global_assets.custom_response import custom_response, custom_response_flask_restful
from flask_restplus import Api, Resource, Namespace, fields
import global_assets.const as CONST

namespace = Namespace(name='insert', path='/', description='insert data json to mysql')


@namespace.route('/insert/add_alert', methods=['POST'])
class add_alert(Resource):
    resource_add_alert = namespace.model('add_alert',
                                         {'alarmRaisedTime': fields.String, 'alarmChangedTime': fields.String,
                                          'alarmClearedTime': fields.String, 'state': fields.String,
                                          'perceivedSeverity': fields.String, 'eventTime': fields.String,
                                          'eventType': fields.String, 'faultType': fields.String,
                                          'probableCause': fields.String, 'isRootCause': fields.String,
                                          'correlatedAlarmId': fields.String, 'faultDetails': fields.String,
                                          'deviceid': fields.String, 'metricid': fields.String})

    @namespace.doc(body=resource_add_alert)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json
        devicedetail = session.query(models.Devicedetail).filter_by(did=data.get('deviceid')).first()
        if devicedetail is None:
            return custom_response_flask_restful(request, 404, "devicedetail chua ton tai", None, None)
        metricdetail = session.query(models.Metricdetail).filter_by(metricid=data.get('metricid')).first()
        if metricdetail is None:
            return custom_response_flask_restful(request, 404, "metricdetail chua ton tai", None, None)

        alert = models.Alert(alarmRaisedTime=data.get('alarmRaisedTime', ""),
                             alarmChangedTime=data.get('alarmChangedTime', ""),
                             alarmClearedTime=data.get('alarmClearedTime', ""), state=data.get('state', ""),
                             perceivedSeverity=data.get('perceivedSeverity', ""), eventTime=data.get('eventTime', ""),
                             eventType=data.get('eventType', ""), faultType=data.get('faultType', ""),
                             probableCause=data.get('probableCause', ""), isRootCause=data.get('isRootCause', ""),
                             correlatedAlarmId=data.get('correlatedAlarmId', ""),
                             faultDetails=data.get('faultDetails', ""), deviceid=data.get('deviceid', ""),
                             metricid=data.get('metricid', ""))

        session.add(alert)
        session.commit()

        res = models.to_json(alert, 'Alert', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)


@namespace.route('/insert/add_devicedetails', methods=['POST'])
class add_devicedetails(Resource):
    resource_add_devicedetails = namespace.model('add_devicedetails', {
        'mode': fields.String, 'status': fields.String, 'errorstring': fields.String, 'timeinterval': fields.String,
        'isprofilebased': fields.Integer, 'fetch_rules': fields.Integer, 'ip': fields.String
    })

    @namespace.doc(body=resource_add_devicedetails)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json



        device = models.Devicedetail(mode=data.get('mode', ""), status=data.get('status', ""),
                                     errorstring=data.get('errorstring', ""), timeinterval=data.get('timeinterval', ""),
                                     last_updated_on= datetime.now(),
                                     isprofilebased=data.get('isprofilebased', ""),
                                     fetch_rules=data.get('fetch_rules', ""), ip=data.get('ip', ""))

        session.add(device)
        session.commit()


        res = models.to_json(device, 'Devicedetail', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)


@namespace.route('/insert/add_groupalerts', methods=['POST'])
class add_groupalerts(Resource):
    resource_add_groupalerts = namespace.model('add_groupalerts', {
        'group_name': fields.String, 'group_desc': fields.String
    })

    @namespace.doc(body=resource_add_groupalerts)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json

        groupalert = models.Groupalert(group_name=data.get('group_name', ""), group_desc=data.get('group_desc', ""))

        session.add(groupalert)
        session.commit()

        res = models.to_json(groupalert, 'Groupalert', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)


@namespace.route('/insert/add_groupdevicepolledatatemplate', methods=['POST'])
class add_groupdevicepolledatatemplate(Resource):
    resource_add_groupdevicepolledatatemplate = namespace.model('add_groupdevicepolledatatemplate',
                                                                {'groupdevices_group_id': fields.String,
                                                                 'polldatatemplate_id': fields.String})

    @namespace.doc(body=resource_add_groupdevicepolledatatemplate)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json
        groupdevices = session.query(models.Groupdevice).filter_by(group_id=data.get('groupdevices_group_id')).first()
        if groupdevices is None:
            return custom_response_flask_restful(request, 404, "groupdevices chua ton tai", None, None)
        polldatatemplate = session.query(models.Polldatatemplate).filter_by(id=data.get('polldatatemplate_id')).first()
        if polldatatemplate is None:
            return custom_response_flask_restful(request, 404, "polldatatemplate chua ton tai", None, None)
        groupdevicepolledatatemplate = models.Groupevicepolledatatemplate(
            groupdevices_group_id=data.get('groupdevices_group_id', ""),
            polldatatemplate_id=data.get('polldatatemplate_id', ""))

        session.add(groupdevicepolledatatemplate)
        session.commit()

        res = models.to_json(groupdevicepolledatatemplate, 'Groupevicepolledatatemplate', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)


@namespace.route('/insert/add_groupdevices', methods=['POST'])
class add_groupdevices(Resource):
    resource_add_groupdevices = namespace.model('add_groupdevices',
                                                {'group_name': fields.String, 'group_desc': fields.String,
                                                 'is_manual': fields.String})

    @namespace.doc(body=resource_add_groupdevices)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json
        groupdevice = models.Groupdevice(group_name=data.get('group_name', ""), group_desc=data.get('group_desc', ""),
                                         is_manual=data.get('is_manual', ""))

        session.add(groupdevice)
        session.commit()

        res = models.to_json(groupdevice, 'Groupdevice', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)


@namespace.route('/insert/add_groupdevicesdevicedetails', methods=['POST'])
class add_groupdevicesdevicedetails(Resource):
    resource_add_groupdevicesdevicedetails = namespace.model('add_groupdevicesdevicedetails',
                                                             {'devicedetail_did': fields.String,
                                                              'groupdevice_id': fields.String})

    @namespace.doc(body=resource_add_groupdevicesdevicedetails)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json
        devicedetails = session.query(models.Devicedetail).filter_by(did=data.get('devicedetail_did')).first()
        if devicedetails is None:
            return custom_response_flask_restful(request, 404, "devicedetails chua ton tai", None, None)

        groupdevices = session.query(models.Groupdevice).filter_by(group_id=data.get('groupdevice_id')).first()
        if groupdevices is None:
            return custom_response_flask_restful(request, 404, "groupdevices chua ton tai", None, None)

        groupdevicesdevicedetail = models.Groupdevicesdevicedetail(devicedetail_did=data.get('devicedetail_did', "")
                                                                   , groupdevice_id=data.get('groupdevice_id', ""))
        session.add(groupdevicesdevicedetail)
        session.commit()

        res = models.to_json(groupdevicesdevicedetail, 'Groupdevicesdevicedetail', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)


@namespace.route('/insert/add_metricdetails', methods=['POST'])
class add_metricdetails(Resource):
    resource_add_metricdetails = namespace.model('add_metricdetails',
                                                 {'metricname': fields.String, 'description': fields.String,
                                                  'displayname': fields.String, 'metrictype': fields.String,
                                                  'datatype': fields.String, 'protocolid': fields.String})

    @namespace.doc(body=resource_add_metricdetails)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json
        protocoldetails = session.query(models.Protocoldetail).filter_by(protocolid=data.get('protocolid')).first()
        if protocoldetails is None:
            return custom_response_flask_restful(request, 404, "protocoldetails chua ton tai", None, None)

        metricdetail = models.Metricdetail(metricname=data.get('metricname', ""),
                                           description=data.get('description', ""),
                                           displayname=data.get('displayname', ""),
                                           metrictype=data.get('metrictype', ""), datatype=data.get('datatype', ""),
                                           protocolid=data.get('protocolid', ""))

        session.add(metricdetail)
        session.commit()

        res = models.to_json(metricdetail, 'Metricdetail', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)


@namespace.route('/insert/add_polldatatemplate', methods=['POST'])
class add_polldatatemplate(Resource):
    resource_add_polldatatemplate = namespace.model('add_polldatatemplate',
                                                    {'name': fields.String, 'agent': fields.String,
                                                     'period': fields.String, 'active': fields.String,
                                                     'oid': fields.String, 'threshold_activate': fields.String,
                                                     'protocol': fields.String, 'metricdetail_id': fields.String,
                                                     'threshold_list_id': fields.String})

    @namespace.doc(body=resource_add_polldatatemplate)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json

        if data.get('metricdetail_id') is None or data.get('threshold_list_id') is None:
            return custom_response_flask_restful(request, 404, "metricdetail_id and threshold_list_id is required", None, None)
        metricdetail = session.query(models.Metricdetail).filter_by(metricid=data.get('metricdetail_id')).first()
        if metricdetail is None:
            return custom_response_flask_restful(request, 404, "metricdetail chua ton tai", None, None)
        threshold_lists = session.query(models.Threshold_list).filter_by(id=data.get('threshold_list_id')).first()
        if threshold_lists is None:
            return custom_response_flask_restful(request, 404, "threshold_lists chua ton tai", None, None)


        check_polldata=  session.query(models.Polldatatemplate).filter_by(metricdetail_id=data.get('metricdetail_id'), threshold_list_id=data.get('threshold_list_id', "")).first()
        if check_polldata is not None:
            return custom_response_flask_restful(request, 404, "polldatatemplate voi metric id: " + str(data.get('metricdetail_id'))  + " threshold_list_id " + str(data.get('threshold_list_id')) + " da ton tai. Please change to update polldatatemplate with id:  "+ str(check_polldata.id)  , None, None)
        polldatatemplate = models.Polldatatemplate(name=data.get('name', ""), agent=data.get('agent', ""),
                                                   period=data.get('period', ""), active=data.get('active', ""),
                                                   oid=data.get('oid', ""),
                                                   threshold_activate=data.get('threshold_activate', ""),
                                                   protocol=data.get('protocol', ""),
                                                   metricdetail_id=data.get('metricdetail_id', ""),
                                                   threshold_list_id=data.get('threshold_list_id', ""))

        session.add(polldatatemplate)
        session.commit()

        res = models.to_json(polldatatemplate, 'Polldatatemplate', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)


@namespace.route('/insert/add_polleddata', methods=['POST'])
class add_polleddata(Resource):
    resource_add_polleddata = namespace.model('add_polleddata',
                                              {'name': fields.String, 'agent': fields.String, 'period': fields.String,
                                               'active': fields.String, 'threshold_activate': fields.String,
                                               'devicedetails_did': fields.String,
                                               'groupdevices_group_id': fields.String,
                                               'threshold_lists_id': fields.String,
                                               'metricdetails_metricid': fields.String})

    @namespace.doc(body=resource_add_polleddata)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json
        metricdetail = session.query(models.Metricdetail).filter_by(metricid=data.get('metricdetails_metricid')).first()
        if metricdetail is None:
            return custom_response_flask_restful(request, 404, "metricdetail chua ton tai", None, None)
        threshold_lists = session.query(models.Threshold_list).filter_by(id=data.get('threshold_lists_id')).first()
        if threshold_lists is None:
            return custom_response_flask_restful(request, 404, "threshold_lists chua ton tai", None, None)

        groupdevices = session.query(models.Groupdevice).filter_by(group_id=data.get('groupdevices_group_id')).first()
        if groupdevices is None:
            return custom_response_flask_restful(request, 404, "groupdevices chua ton tai", None, None)

        devicedetails = session.query(models.Devicedetail).filter_by(did=data.get('devicedetails_did')).first()
        if devicedetails is None:
            return custom_response_flask_restful(request, 404, "devicedetails chua ton tai", None, None)

        polleddata = models.Polleddata(name=data.get('name', ""), agent=data.get('agent', ""),
                                       period=data.get('period', ""), active=data.get('active', ""),
                                       threshold_activate=data.get('threshold_activate', ""),
                                       devicedetails_did=data.get('devicedetails_did', ""),
                                       groupdevices_group_id=data.get('groupdevices_group_id', ""),
                                       threshold_lists_id=data.get('threshold_lists_id', ""),
                                       metricdetails_metricid=data.get('metricdetails_metricid', ""))

        session.add(polleddata)
        session.commit()

        res = models.to_json(polleddata, 'Polleddata', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)


@namespace.route('/insert/add_protocoldetails', methods=['POST'])
class add_protocoldetails(Resource):
    resource_add_protocoldetails = namespace.model('add_protocoldetails', {'protocolname': fields.String})

    @namespace.doc(body=resource_add_protocoldetails)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json


        protocoldetail = models.Protocoldetail(protocolname=data.get('protocolname', ""))

        session.add(protocoldetail)
        session.commit()
        new_protocoldetail = models.Protocoldetail(protocolname=data.get('protocolname', ""))
        res = models.to_json(protocoldetail, 'Protocoldetail', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)


@namespace.route('/insert/add_threshold_lists', methods=['POST'])
class add_threshold_lists(Resource):
    resource_add_threshold_lists = namespace.model('add_threshold_lists', {'description': fields.String})

    @namespace.doc(body=resource_add_threshold_lists)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json


        threshold_list = models.Threshold_list(description=data.get('description', ""))

        session.add(threshold_list)
        session.commit()

        res = models.to_json(threshold_list, 'Threshold_list', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)


@namespace.route('/insert/add_thresholdobjects', methods=['POST'])
class add_thresholdobjects(Resource):
    resource_add_thresholdobjects = namespace.model('add_thresholdobjects',
                                                    {'name': fields.String, 'kind': fields.String,
                                                     'priority': fields.String, 'category': fields.String,
                                                     'thresholdvalue': fields.String, 'rearmvalue': fields.String,
                                                     'mmessage': fields.String, 'allowed': fields.String,
                                                     'is_customize': fields.String, 'consecutive_time': fields.String,
                                                     'operator': fields.String, 'severity': fields.String, 'threshold_lists_id':fields.String})

    @namespace.doc(body=resource_add_thresholdobjects)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json
        threshold_lists = session.query(models.Threshold_list).filter_by(id=data.get('threshold_lists_id')).first()
        if threshold_lists is None:
            return custom_response_flask_restful(request, 404, "threshold_lists chua ton tai", None, None)

        thresholdobject = models.Thresholdobject(name=data.get('name', ""), kind=data.get('kind', ""),
                                                 priority=data.get('priority', ""), category=data.get('category', ""),
                                                 thresholdvalue=data.get('thresholdvalue', ""),
                                                 rearmvalue=data.get('rearmvalue', ""),
                                                 mmessage=data.get('mmessage', ""), allowed=data.get('allowed', ""),
                                                 is_customize=data.get('is_customize', ""),
                                                 consecutive_time=data.get('consecutive_time', ""),
                                                 operator=data.get('operator', ""), severity=data.get('severity', "")
                                                 , threshold_lists_id=data.get('threshold_lists_id', "")
                                                 )

        session.add(thresholdobject)
        session.commit()

        res = models.to_json(thresholdobject, 'Thresholdobject', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)
