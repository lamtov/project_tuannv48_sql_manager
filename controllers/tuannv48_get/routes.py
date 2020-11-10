from flask import Blueprint, abort, request, redirect, url_for
from sqlalchemy import and_
from .assets import *

from global_assets.custom_response import custom_response, custom_response_flask_restful
from flask_restplus import Api, Resource,Namespace

namespace = Namespace(name='get',path='/',description='get host info')
@namespace.route('/alert', methods=['GET'])
class Getting_Alert(Resource):
    @namespace.response(200, 'Information of all alert in database')
    def get(self):
        alert = session.query(models.Alert).all()
        res = models.to_json(alert, 'Alert', True)
        return custom_response_flask_restful(request, 200, None, None, res)

@namespace.route('/alert/<string:alertid>', methods=['GET'])
class Getting_alert_id(Resource):
    @namespace.response(200, 'Information of one alert in database')
    def get(self,alertid):
        alert = session.query(models.Alert).filter_by(alertid=alertid).first()
        session.commit()
        if alert is None:
            abort(400)

        return custom_response_flask_restful(request, 200, None, None, models.to_json(alert, 'Alert', False))


@namespace.route('/devicedetails', methods=['GET'])
class Getting_Devicedetail(Resource):
    @namespace.response(200, 'Information of all devicedetails in database')
    def get(self):
        devicedetails = session.query(models.Devicedetail).all()
        res = models.to_json(devicedetails, 'Devicedetail', True)
        return custom_response_flask_restful(request, 200, None, None, res)

@namespace.route('/devicedetails/<string:did>', methods=['GET'])
class Getting_Devicedetail_id(Resource):
    @namespace.response(200, 'Information of one Devicedetail in database')
    def get(self,did):
        devicedetails = session.query(models.Devicedetail).filter_by(did=did).first()
        session.commit()
        if devicedetails is None:
            abort(400)

        return custom_response_flask_restful(request, 200, None, None, models.to_json(devicedetails, 'Devicedetail', False))



@namespace.route('/groupalerts', methods=['GET'])
class Getting_Groupalert(Resource):
    @namespace.response(200, 'Information of all groupalerts in database')
    def get(self):
        groupalerts = session.query(models.Groupalert).all()
        res = models.to_json(groupalerts, 'Groupalert', True)
        return custom_response_flask_restful(request, 200, None, None, res)

@namespace.route('/groupalerts/<string:group_id>', methods=['GET'])
class Getting_Groupalert_id(Resource):
    @namespace.response(200, 'Information of one Groupalert in database')
    def get(self,group_id):
        groupalerts = session.query(models.Groupalert).filter_by(group_id=group_id).first()
        session.commit()
        if groupalerts is None:
            abort(400)

        return custom_response_flask_restful(request, 200, None, None, models.to_json(groupalerts, 'Groupalert', False))



@namespace.route('/groupdevicepolledatatemplate', methods=['GET'])
class Getting_Groupevicepolledatatemplate(Resource):
    @namespace.response(200, 'Information of all groupdevicepolledatatemplate in database')
    def get(self):
        groupdevicepolledatatemplate = session.query(models.Groupevicepolledatatemplate).all()
        res = models.to_json(groupdevicepolledatatemplate, 'Groupevicepolledatatemplate', True)
        return custom_response_flask_restful(request, 200, None, None, res)

@namespace.route('/groupdevicepolledatatemplate/<string:id>', methods=['GET'])
class Getting_Groupevicepolledatatemplate_id(Resource):
    @namespace.response(200, 'Information of one Groupevicepolledatatemplate in database')
    def get(self,id):
        groupdevicepolledatatemplate = session.query(models.Groupevicepolledatatemplate).filter_by(id=id).first()
        session.commit()
        if groupdevicepolledatatemplate is None:
            abort(400)

        return custom_response_flask_restful(request, 200, None, None, models.to_json(groupdevicepolledatatemplate, 'Groupevicepolledatatemplate', False))

@namespace.route('/groupdevices', methods=['GET'])
class Getting_Groupdevice(Resource):
    @namespace.response(200, 'Information of all groupdevices in database')
    def get(self):
        groupdevices = session.query(models.Groupdevice).all()
        res = models.to_json(groupdevices, 'Groupdevice', True)
        return custom_response_flask_restful(request, 200, None, None, res)

@namespace.route('/groupdevices/<string:group_id>', methods=['GET'])
class Getting_Groupdevice_id(Resource):
    @namespace.response(200, 'Information of one Groupdevice in database')
    def get(self,group_id):
        groupdevices = session.query(models.Groupdevice).filter_by(group_id=group_id).first()
        session.commit()
        if groupdevices is None:
            abort(400)

        return custom_response_flask_restful(request, 200, None, None, models.to_json(groupdevices, 'Groupdevice', False))


@namespace.route('/groupdevicesdevicedetails', methods=['GET'])
class Getting_Groupdevicesdevicedetail(Resource):
    @namespace.response(200, 'Information of all groupdevicesdevicedetails in database')
    def get(self):
        groupdevicesdevicedetails = session.query(models.Groupdevicesdevicedetail).all()
        res = models.to_json(groupdevicesdevicedetails, 'Groupdevicesdevicedetail', True)
        return custom_response_flask_restful(request, 200, None, None, res)

@namespace.route('/groupdevicesdevicedetails/<string:id>', methods=['GET'])
class Getting_Groupdevicesdevicedetail_id(Resource):
    @namespace.response(200, 'Information of one Groupdevicesdevicedetail in database')
    def get(self,id):
        groupdevicesdevicedetails = session.query(models.Groupdevicesdevicedetail).filter_by(id=id).first()
        session.commit()
        if groupdevicesdevicedetails is None:
            abort(400)

        return custom_response_flask_restful(request, 200, None, None, models.to_json(groupdevicesdevicedetails, 'Groupdevicesdevicedetail', False))


@namespace.route('/metricdetails', methods=['GET'])
class Getting_Metricdetail(Resource):
    @namespace.response(200, 'Information of all metricdetails in database')
    def get(self):
        metricdetails = session.query(models.Metricdetail).all()
        res = models.to_json(metricdetails, 'Metricdetail', True)
        return custom_response_flask_restful(request, 200, None, None, res)

@namespace.route('/metricdetails/<string:metricid>', methods=['GET'])
class Getting_Metricdetail_id(Resource):
    @namespace.response(200, 'Information of one Metricdetail in database')
    def get(self,metricid):
        metricdetails = session.query(models.Metricdetail).filter_by(metricid=metricid).first()
        session.commit()
        if metricdetails is None:
            abort(400)

        return custom_response_flask_restful(request, 200, None, None, models.to_json(metricdetails, 'Metricdetail', False))



@namespace.route('/polldatatemplate', methods=['GET'])
class Getting_Polldatatemplate(Resource):
    @namespace.response(200, 'Information of all polldatatemplate in database')
    def get(self):
        polldatatemplate = session.query(models.Polldatatemplate).all()
        res = models.to_json(polldatatemplate, 'Polldatatemplate', True)
        return custom_response_flask_restful(request, 200, None, None, res)

@namespace.route('/polldatatemplate/<string:id>', methods=['GET'])
class Getting_Polldatatemplate_id(Resource):
    @namespace.response(200, 'Information of one Polldatatemplate in database')
    def get(self,id):
        polldatatemplate = session.query(models.Polldatatemplate).filter_by(id=id).first()
        session.commit()
        if polldatatemplate is None:
            abort(400)

        return custom_response_flask_restful(request, 200, None, None, models.to_json(polldatatemplate, 'Polldatatemplate', False))




@namespace.route('/polleddata', methods=['GET'])
class Getting_Polleddata(Resource):
    @namespace.response(200, 'Information of all polleddata in database')
    def get(self):
        polleddata = session.query(models.Polleddata).all()
        res = models.to_json(polleddata, 'Polleddata', True)
        return custom_response_flask_restful(request, 200, None, None, res)

@namespace.route('/polleddata/<string:id>', methods=['GET'])
class Getting_Polleddata_id(Resource):
    @namespace.response(200, 'Information of one Polleddata in database')
    def get(self,id):
        polleddata = session.query(models.Polleddata).filter_by(id=id).first()
        session.commit()
        if polleddata is None:
            abort(400)

        return custom_response_flask_restful(request, 200, None, None, models.to_json(polleddata, 'Polleddata', False))



@namespace.route('/protocoldetails', methods=['GET'])
class Getting_Protocoldetail(Resource):
    @namespace.response(200, 'Information of all protocoldetails in database')
    def get(self):
        protocoldetails = session.query(models.Protocoldetail).all()
        res = models.to_json(protocoldetails, 'Protocoldetail', True)
        return custom_response_flask_restful(request, 200, None, None, res)

@namespace.route('/protocoldetails/<string:protocolid>', methods=['GET'])
class Getting_Protocoldetail_id(Resource):
    @namespace.response(200, 'Information of one Protocoldetail in database')
    def get(self,protocolid):
        protocoldetails = session.query(models.Protocoldetail).filter_by(protocolid=protocolid).first()
        session.commit()
        if protocoldetails is None:
            abort(400)

        return custom_response_flask_restful(request, 200, None, None, models.to_json(protocoldetails, 'Protocoldetail', False))





@namespace.route('/threshold_lists', methods=['GET'])
class Getting_Threshold_list(Resource):
    @namespace.response(200, 'Information of all threshold_lists in database')
    def get(self):
        threshold_lists = session.query(models.Threshold_list).all()
        res = models.to_json(threshold_lists, 'Threshold_list', True)
        return custom_response_flask_restful(request, 200, None, None, res)

@namespace.route('/threshold_lists/<string:id>', methods=['GET'])
class Getting_Threshold_list_id(Resource):
    @namespace.response(200, 'Information of one Threshold_list in database')
    def get(self,id):
        threshold_lists = session.query(models.Threshold_list).filter_by(id=id).first()
        session.commit()
        if threshold_lists is None:
            abort(400)

        return custom_response_flask_restful(request, 200, None, None, models.to_json(threshold_lists, 'Threshold_list', False))





@namespace.route('/thresholdobjects', methods=['GET'])
class Getting_Thresholdobject(Resource):
    @namespace.response(200, 'Information of all thresholdobjects in database')
    def get(self):
        thresholdobjects = session.query(models.Thresholdobject).all()
        res = models.to_json(thresholdobjects, 'Thresholdobject', True)
        return custom_response_flask_restful(request, 200, None, None, res)
@namespace.route('/thresholdobjects/<string:id>', methods=['GET'])
class Getting_Thresholdobject_id(Resource):
    @namespace.response(200, 'Information of one Thresholdobject in database')
    def get(self,id):
        thresholdobjects = session.query(models.Thresholdobject).filter_by(id=id).first()
        session.commit()
        if thresholdobjects is None:
            abort(400)

        return custom_response_flask_restful(request, 200, None, None, models.to_json(thresholdobjects, 'Thresholdobject', False))