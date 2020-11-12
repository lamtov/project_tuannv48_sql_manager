from flask import Blueprint, abort, request
from sqlalchemy import or_
from .assets import *

from global_assets.custom_response import custom_response, custom_response_flask_restful
from flask_restplus import Api, Resource, Namespace, fields
import global_assets.const as CONST

namespace = Namespace(name='api', path='/', description='list api tuannv48')


@namespace.route('/api/create_template', methods=['POST'])
class create_template(Resource):
    resource_create_template = namespace.model('create_template',
                                         {'group_name': fields.String, 'group_desc': fields.String,
                                          'metricid': fields.String, 'threshold_value_1': fields.String,
                                          'threshold_value_2': fields.String, 'threshold_value_3': fields.String,
                                          'threshold_value_4': fields.String, 'rearmvalue': fields.String})

    @namespace.doc(body=resource_create_template)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json
        if data.get("rearmvalue") is None:
            return custom_response_flask_restful(request, 404, "rearmvalue phai duoc set", None, None)
        metricdetail = session.query(models.Metricdetail).filter_by(metricid=data.get('metricid')).first()
        if metricdetail is None:
            return custom_response_flask_restful(request, 404, "metricdetail chua ton tai", None, None)

        groupdevice = session.query(models.Groupdevice).filter_by(group_name=data.get('group_name')).first()
        if groupdevice is None:
            groupdevice = models.Groupdevice(group_name=data.get('group_name', ""),
                                             group_desc=data.get('group_name', ""),
                                             is_manual=False)

            session.add(groupdevice)
            session.commit()

        threshold_list = models.Threshold_list( description=str('threshold_list_for ' + metricdetail.displayname + ' of '+ data.get('group_name', "")))
        session.add(threshold_list)
        session.commit()

        for id in range(1,5):
            if data.get('threshold_value_' + str(id)):

                thresholdobject = models.Thresholdobject(name='threshold_template_'+data.get('group_name', ""), kind="long",
                                                 priority=id,
                                                 thresholdvalue=data.get('threshold_value_' + str(id)),
                                                 rearmvalue=data.get('rearmvalue', ""),operator='operator',
                                                 is_customize=False, threshold_lists_id=threshold_list.id
                                                 )
                session.add(thresholdobject)
                session.commit()

        polldatatemplate = models.Polldatatemplate(name='threshold_template_'+data.get('group_name', ""),
                                                  active=True,

                                                   threshold_activate=True,
                                                   metricdetail_id=data.get('metricid'),
                                                   threshold_list_id=threshold_list.id)

        session.add(polldatatemplate)
        session.commit()

        groupdevicepolledatatemplate = models.Groupevicepolledatatemplate(
            groupdevices_group_id=groupdevice.group_id,
            polldatatemplate_id=polldatatemplate.id)

        session.add(groupdevicepolledatatemplate)
        session.commit()


        res = models.to_json(groupdevicepolledatatemplate, 'Groupevicepolledatatemplate', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, 'Ok roi nhe, check in /api/v1/threshold_lists and /api/v1/groupdevices', res)



@namespace.route('/api/add_threshold_to_template', methods=['POST'])
class add_threshold_to_template(Resource):
    resource_add_threshold_to_template = namespace.model('add_threshold_to_template',
                                         {'group_id': fields.String,
                                          'metricid': fields.String, 'threshold_value_1': fields.String,
                                          'threshold_value_2': fields.String, 'threshold_value_3': fields.String,
                                          'threshold_value_4': fields.String, 'rearmvalue': fields.String})

    @namespace.doc(body=resource_add_threshold_to_template)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json
        if data.get("rearmvalue") is None:
            return custom_response_flask_restful(request, 404, "rearmvalue phai duoc set", None, None)
        metricdetail = session.query(models.Metricdetail).filter_by(metricid=data.get('metricid')).first()
        if metricdetail is None:
            return custom_response_flask_restful(request, 404, "metricdetail chua ton tai", None, None)

        groupdevice = session.query(models.Groupdevice).filter_by(group_id=data.get('group_id')).first()
        if groupdevice is None:
            return custom_response_flask_restful(request, 404, "groupdevice chua ton tai", None, None)



        list_groupdevicepolledatatemplates =session.query(models.Groupevicepolledatatemplate).filter_by(groupdevices_group_id=data.get('group_id')).all()

        for groupdevicepolledatatemplate in list_groupdevicepolledatatemplates:
            if groupdevicepolledatatemplate.groupdevices_group_id==data.get('group_id'):
                polldatatemplate_id = groupdevicepolledatatemplate.polldatatemplate_id
                polldatatemplate_ex=session.query(models.Polldatatemplate).filter_by(id=polldatatemplate_id, metricdetail_id=data.get('metricid') ,active=1).first()
                if polldatatemplate_ex is not None:
                    threshold_list_id=polldatatemplate_ex.threshold_list_id
                    threshold_list=session.query(models.Threshold_list).filter_by( id=threshold_list_id).first()
                    if threshold_list is None:
                        return custom_response_flask_restful(request, 404, "threshold_list chua ton tai", None,None)
                    else:
                        for id in range(1, 5):
                            if data.get('threshold_value_' + str(id)):
                                thresholdobject = models.Thresholdobject(
                                    name='threshold_template_' + data.get('group_name', ""), kind="long",
                                    priority=id,
                                    thresholdvalue=data.get('threshold_value_' + str(id)),
                                    rearmvalue=data.get('rearmvalue', ""), operator='operator',
                                    is_customize=False, threshold_lists_id=threshold_list.id
                                    )
                                session.add(thresholdobject)
                                session.commit()
                    res = models.to_json(threshold_list, 'Threshold_list', False)
                    session.close()
                    return custom_response_flask_restful(request, 201, None, 'Ok roi nhe, check in http://127.0.0.1:1234/api/v1/threshold_lists/'+ str(threshold_list.id), res)
                else:
                    return custom_response_flask_restful(request, 404, "polldatatemplate_ex chua ton tai", None, None)

        res = models.to_json(groupdevice, 'Groupdevice', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)


@namespace.route('/api/get_template', methods=['GET'])
class get_template(Resource):
    @namespace.doc(params={'group_id':"",'metricid':"" })
    @namespace.response(200, '/api/v1/api/get_template?group_id=xxxx&metricid=yyyy')
    def get(self):
        if not (request.args.get('group_id') or request.args.get('metricid')):
            abort(400)

        data = {'group_id':int(request.args.get('group_id')),'metricid':int(request.args.get('metricid')) }

        metricdetail = session.query(models.Metricdetail).filter_by(metricid=data.get('metricid')).first()
        if metricdetail is None:
            return custom_response_flask_restful(request, 404, "metricdetail chua ton tai", None, None)

        groupdevice = session.query(models.Groupdevice).filter_by(group_id=data.get('group_id')).first()
        if groupdevice is None:
            return custom_response_flask_restful(request, 404, "groupdevice chua ton tai", None, None)

        list_groupdevicepolledatatemplates =session.query(models.Groupevicepolledatatemplate).filter_by(groupdevices_group_id=data.get('group_id')).all()
        print(list_groupdevicepolledatatemplates)
        for groupdevicepolledatatemplate in list_groupdevicepolledatatemplates:
            if groupdevicepolledatatemplate.groupdevices_group_id==data.get('group_id'):
                polldatatemplate_id = groupdevicepolledatatemplate.polldatatemplate_id

                polldatatemplate_ex=session.query(models.Polldatatemplate).filter_by(id=polldatatemplate_id, metricdetail_id=data.get('metricid') ,active=1).first()
                if polldatatemplate_ex is not None:

                    threshold_list_id=polldatatemplate_ex.threshold_list_id
                    threshold_list=session.query(models.Threshold_list).filter_by( id=threshold_list_id).first()
                    if threshold_list is None:
                        return custom_response_flask_restful(request, 404, "threshold_list chua ton tai", None,None)
                    else:
                        thresholdobjects = threshold_list.thresholdobjects
                        res_json={
                            'metricdetail':models.to_json(metricdetail, 'Metricdetail', False),
                            'groupdevice':models.to_json(groupdevice, 'Groupdevice', False),
                            'polldatatemplate_ex':models.to_json(polldatatemplate_ex, 'Polldatatemplate', False),
                            'threshold_list':models.to_json(threshold_list, 'Threshold_list', False),
                            'thresholdobjects':models.to_json(thresholdobjects, 'Thresholdobject', True)
                        }

                    session.close()
                    return custom_response_flask_restful(request, 201, None, 'Ok roi nhe', res_json)
                else:
                    res_json = {
                        'metricdetail': models.to_json(metricdetail, 'Metricdetail', False),
                        'groupdevice': models.to_json(groupdevice, 'Groupdevice', False),
                    }
                    return custom_response_flask_restful(request, 404, "polldatatemplate_ex chua ton tai", None, res_json)

        res_json = {
            'metricdetail': models.to_json(metricdetail, 'Metricdetail', False),
            'groupdevice': models.to_json(groupdevice, 'Groupdevice', False),
        }
        session.close()
        return custom_response_flask_restful(request, 201, "Some thing wrong, try again", None, res_json)


@namespace.route('/api/update_threshold_in_template', methods=['POST'])
class update_threshold_in_template(Resource):
    resource_update_threshold_in_template = namespace.model('update_threshold_in_template',
                                         {'group_id': fields.String,
                                          'metricid': fields.String, 'threshold_value_1': fields.String,
                                          'threshold_value_2': fields.String, 'threshold_value_3': fields.String,
                                          'threshold_value_4': fields.String, 'rearmvalue': fields.String})

    @namespace.doc(body=resource_update_threshold_in_template)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json
        if data.get("rearmvalue") is None:
            return custom_response_flask_restful(request, 404, "rearmvalue phai duoc set", None, None)
        metricdetail = session.query(models.Metricdetail).filter_by(metricid=data.get('metricid')).first()
        if metricdetail is None:
            return custom_response_flask_restful(request, 404, "metricdetail chua ton tai", None, None)

        groupdevice = session.query(models.Groupdevice).filter_by(group_id=data.get('group_id')).first()
        if groupdevice is None:
            return custom_response_flask_restful(request, 404, "groupdevice chua ton tai", None, None)



        list_groupdevicepolledatatemplates =session.query(models.Groupevicepolledatatemplate).filter_by(groupdevices_group_id=data.get('group_id')).all()

        for groupdevicepolledatatemplate in list_groupdevicepolledatatemplates:
            if groupdevicepolledatatemplate.groupdevices_group_id==data.get('group_id'):
                polldatatemplate_id = groupdevicepolledatatemplate.polldatatemplate_id
                polldatatemplate_ex=session.query(models.Polldatatemplate).filter_by(id=polldatatemplate_id, metricdetail_id=data.get('metricid') ,active=1).first()
                if polldatatemplate_ex is not None:
                    threshold_list_id=polldatatemplate_ex.threshold_list_id
                    threshold_list=session.query(models.Threshold_list).filter_by( id=threshold_list_id).first()
                    if threshold_list is None:
                        return custom_response_flask_restful(request, 404, "threshold_list chua ton tai", None,None)
                    else:
                        thresholdobjects = threshold_list.thresholdobjects
                        for thesholdobject in thresholdobjects:
                            session.delete(thesholdobject)
                        session.commit()

                        for id in range(1, 5):
                            if data.get('threshold_value_' + str(id)):
                                thresholdobject = models.Thresholdobject(
                                    name='threshold_template_' + data.get('group_name', ""), kind="long",
                                    priority=id,
                                    thresholdvalue=data.get('threshold_value_' + str(id)),
                                    rearmvalue=data.get('rearmvalue', ""), operator='operator',
                                    is_customize=False, threshold_lists_id=threshold_list.id
                                    )
                                session.add(thresholdobject)
                        session.commit()
                    res = models.to_json(threshold_list, 'Threshold_list', False)
                    session.close()
                    return custom_response_flask_restful(request, 201, None, 'Ok roi nhe, check in http://127.0.0.1:1234/api/v1/threshold_lists/'+ str(threshold_list.id), res)
                else:
                    return custom_response_flask_restful(request, 404, "polldatatemplate_ex chua ton tai", None, None)

        res = models.to_json(groupdevice, 'Groupdevice', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)



@namespace.route('/api/delete_threshold_in_template', methods=['POST'])
class delete_threshold_in_template(Resource):
    resource_delete_threshold_in_template = namespace.model('delete_threshold_in_template',
                                         {'group_id': fields.String,
                                          'metricid': fields.String,
                                          'threshold_id':fields.String})

    @namespace.doc(body=resource_delete_threshold_in_template)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json

        metricdetail = session.query(models.Metricdetail).filter_by(metricid=data.get('metricid')).first()
        if metricdetail is None:
            return custom_response_flask_restful(request, 404, "metricdetail chua ton tai", None, None)

        groupdevice = session.query(models.Groupdevice).filter_by(group_id=data.get('group_id')).first()
        if groupdevice is None:
            return custom_response_flask_restful(request, 404, "groupdevice chua ton tai", None, None)



        list_groupdevicepolledatatemplates =session.query(models.Groupevicepolledatatemplate).filter_by(groupdevices_group_id=data.get('group_id')).all()

        for groupdevicepolledatatemplate in list_groupdevicepolledatatemplates:
            if groupdevicepolledatatemplate.groupdevices_group_id==data.get('group_id'):
                polldatatemplate_id = groupdevicepolledatatemplate.polldatatemplate_id
                polldatatemplate_ex=session.query(models.Polldatatemplate).filter_by(id=polldatatemplate_id, metricdetail_id=data.get('metricid') ,active=1).first()
                if polldatatemplate_ex is not None:
                    threshold_list_id=polldatatemplate_ex.threshold_list_id
                    threshold_list=session.query(models.Threshold_list).filter_by( id=threshold_list_id).first()
                    if threshold_list is None:
                        return custom_response_flask_restful(request, 404, "threshold_list chua ton tai", None,None)
                    else:
                        thresholdobject = session.query(models.Thresholdobject).filter_by(id=data.get('threshold_id'),threshold_lists_id=threshold_list.id).first()
                        if thresholdobject  is None:
                            return custom_response_flask_restful(request, 404, "thresholdobject chua ton tai", None,None)
                        else:
                            session.delete(thresholdobject)
                            session.commit()
                    res = models.to_json(threshold_list, 'Threshold_list', False)
                    session.close()
                    return custom_response_flask_restful(request, 201, None, 'Ok roi nhe, check in http://127.0.0.1:1234/api/v1/threshold_lists/'+ str(threshold_list.id), res)
                else:
                    return custom_response_flask_restful(request, 404, "polldatatemplate_ex chua ton tai", None, None)

        res = models.to_json(groupdevice, 'Groupdevice', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)


@namespace.route('/api/update_value_list_metrics', methods=['POST'])
class update_value_list_metrics(Resource):
    resource_update_value_list_metrics= namespace.model('update_value_list_metrics',
                                         {'threshold_list_id': fields.String,'threshold_value_1': fields.String,
                                          'threshold_value_2': fields.String, 'threshold_value_3': fields.String,
                                          'threshold_value_4': fields.String, 'rearmvalue': fields.String})

    @namespace.doc(body=resource_update_value_list_metrics)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json

        if data.get("rearmvalue") is None:
            return custom_response_flask_restful(request, 404, "rearmvalue phai duoc set", None, None)

        threshold_list = session.query(models.Threshold_list).filter_by(id=data.get('threshold_list_id')).first()
        if threshold_list is None:
            return custom_response_flask_restful(request, 404, "threshold_list chua ton tai", None, None)
        thresholdobjects = threshold_list.thresholdobjects
        for i in range(0, len(thresholdobjects)):
            thresholdobjects[i].thresholdvalue=data.get('threshold_value_' + str(i+1))
            thresholdobjects[i].rearmvalue= data.get('rearmvalue')

        session.add(threshold_list)
        session.commit()


        res = models.to_json(threshold_list, 'Threshold_list', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)







@namespace.route('/api/create_threshold', methods=['POST'])
class create_threshold(Resource):
    resource_create_threshold = namespace.model('create_threshold',
                                         {'device_name': fields.String, 'device_ip': fields.String,
                                          'metricid': fields.String, 'threshold_value_1': fields.String,
                                          'threshold_value_2': fields.String, 'threshold_value_3': fields.String,
                                          'threshold_value_4': fields.String, 'rearmvalue': fields.String})

    @namespace.doc(body=resource_create_threshold)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json

        metricdetail = session.query(models.Metricdetail).filter_by(metricid=data.get('metricid')).first()
        if metricdetail is None:
            return custom_response_flask_restful(request, 404, "metricdetail chua ton tai", None, None)

        device = session.query(models.Devicedetail).filter_by(mode=data.get('device_name', "")).first()
        if device is None:
            device = models.Devicedetail(mode=data.get('device_name', ""),isprofilebased=False,ip=data.get('device_ip', ""))

            session.add(device)
            session.commit()

        threshold_list = models.Threshold_list( description=str('threshold_list_for ' + metricdetail.displayname + ' of '+ data.get('device_name', "")))
        session.add(threshold_list)
        session.commit()

        for id in range(1,5):
            if data.get('threshold_value_' + str(id)):

                thresholdobject = models.Thresholdobject(name='threshold_template_'+data.get('group_name', ""), kind="long",
                                                 priority=id,
                                                 thresholdvalue=data.get('threshold_value_' + str(id)),
                                                 rearmvalue=data.get('rearmvalue', ""),operator='operator',
                                                 is_customize=False, threshold_lists_id=threshold_list.id
                                                 )
                session.add(thresholdobject)
                session.commit()

        default_groupdevice = session.query(models.Groupdevice).first()

        polleddata = models.Polleddata(name='polleddata for ' + data.get('device_name' , ""),
                                       active=True,
                                       threshold_activate=True,
                                       devicedetails_did=device.did,
                                       groupdevices_group_id=default_groupdevice.group_id,
                                       threshold_lists_id=threshold_list.id,
                                       metricdetails_metricid=metricdetail.metricid)

        session.add(polleddata)
        session.commit()

        res = models.to_json(polleddata, 'Polleddata', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, None, res)

@namespace.route('/api/add_threshold_to_device', methods=['POST'])
class add_threshold_to_device(Resource):
    resource_add_threshold_to_device = namespace.model('add_threshold_to_device',
                                         {'device_id':fields.String,
                                          'metricid': fields.String, 'threshold_value_1': fields.String,
                                          'threshold_value_2': fields.String, 'threshold_value_3': fields.String,
                                          'threshold_value_4': fields.String, 'rearmvalue': fields.String})

    @namespace.doc(body=resource_add_threshold_to_device)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json
        if data.get("rearmvalue") is None:
            return custom_response_flask_restful(request, 404, "rearmvalue phai duoc set", None, None)
        metricdetail = session.query(models.Metricdetail).filter_by(metricid=data.get('metricid')).first()
        if metricdetail is None:
            return custom_response_flask_restful(request, 404, "metricdetail chua ton tai", None, None)

        device = session.query(models.Devicedetail).filter_by(did=data.get('device_id', "")).first()
        if device is None:
            return custom_response_flask_restful(request, 404, "device chua ton tai", None, None)
        polleddata = session.query(models.Polleddata).filter_by(devicedetails_did=device.did, metricdetails_metricid=metricdetail.metricid).first()
        if polleddata is None:
            return custom_response_flask_restful(request, 404, "polleddata chua ton tai", None, None)


        threshold_list_id = polleddata.threshold_lists_id
        threshold_list = session.query(models.Threshold_list).filter_by(id=threshold_list_id).first()
        if threshold_list is None:
            return custom_response_flask_restful(request, 404, "threshold_list chua ton tai", None, None)
        else:
            for id in range(1, 5):
                if data.get('threshold_value_' + str(id)):
                    thresholdobject = models.Thresholdobject(
                        name='threshold_template_' + data.get('group_name', ""), kind="long",
                        priority=id,
                        thresholdvalue=data.get('threshold_value_' + str(id)),
                        rearmvalue=data.get('rearmvalue', ""), operator='operator',
                        is_customize=False, threshold_lists_id=threshold_list.id
                    )
                    session.add(thresholdobject)
            session.commit()
        res = models.to_json(threshold_list, 'Threshold_list', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, 'Ok roi nhe, check in http://127.0.0.1:1234/api/v1/threshold_lists/'+ str(threshold_list.id), res)


@namespace.route('/api/update_threshold_to_device', methods=['POST'])
class update_threshold_to_device(Resource):
    resource_update_threshold_to_device = namespace.model('update_threshold_to_device',
                                         {'device_id':fields.String,
                                          'metricid': fields.String, 'threshold_value_1': fields.String,
                                          'threshold_value_2': fields.String, 'threshold_value_3': fields.String,
                                          'threshold_value_4': fields.String, 'rearmvalue': fields.String})

    @namespace.doc(body=resource_update_threshold_to_device)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json
        if data.get("rearmvalue") is None:
            return custom_response_flask_restful(request, 404, "rearmvalue phai duoc set", None, None)
        metricdetail = session.query(models.Metricdetail).filter_by(metricid=data.get('metricid')).first()
        if metricdetail is None:
            return custom_response_flask_restful(request, 404, "metricdetail chua ton tai", None, None)

        device = session.query(models.Devicedetail).filter_by(did=data.get('device_id', "")).first()
        if device is None:
            return custom_response_flask_restful(request, 404, "device chua ton tai", None, None)
        polleddata = session.query(models.Polleddata).filter_by(devicedetails_did=device.did, metricdetails_metricid=metricdetail.metricid).first()
        if polleddata is None:
            return custom_response_flask_restful(request, 404, "polleddata chua ton tai", None, None)


        threshold_list_id = polleddata.threshold_lists_id
        threshold_list = session.query(models.Threshold_list).filter_by(id=threshold_list_id).first()
        if threshold_list is None:
            return custom_response_flask_restful(request, 404, "threshold_list chua ton tai", None, None)
        else:
            thresholdobjects = threshold_list.thresholdobjects
            for thesholdobject in thresholdobjects:
                session.delete(thesholdobject)
            session.commit()
            for id in range(1, 5):
                if data.get('threshold_value_' + str(id)):
                    thresholdobject = models.Thresholdobject(
                        name='threshold_template_' + data.get('group_name', ""), kind="long",
                        priority=id,
                        thresholdvalue=data.get('threshold_value_' + str(id)),
                        rearmvalue=data.get('rearmvalue', ""), operator='operator',
                        is_customize=False, threshold_lists_id=threshold_list.id
                    )
                    session.add(thresholdobject)
            session.commit()
        res = models.to_json(threshold_list, 'Threshold_list', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, 'Ok roi nhe, check in http://127.0.0.1:1234/api/v1/threshold_lists/'+ str(threshold_list.id), res)

@namespace.route('/api/delete_threshold_in_device', methods=['POST'])
class delete_threshold_in_device(Resource):
    resource_delete_threshold_in_device = namespace.model('delete_threshold_in_device',
                                         {'device_id':fields.String,
                                          'metricid': fields.String, 'threshold_id': fields.String})

    @namespace.doc(body=resource_delete_threshold_in_device)
    def post(self):
        if not request.json:
            abort(400)
        else:
            data = request.json

        metricdetail = session.query(models.Metricdetail).filter_by(metricid=data.get('metricid')).first()
        if metricdetail is None:
            return custom_response_flask_restful(request, 404, "metricdetail chua ton tai", None, None)

        device = session.query(models.Devicedetail).filter_by(did=data.get('device_id', "")).first()
        if device is None:
            return custom_response_flask_restful(request, 404, "device chua ton tai", None, None)
        polleddata = session.query(models.Polleddata).filter_by(devicedetails_did=device.did, metricdetails_metricid=metricdetail.metricid).first()
        if polleddata is None:
            return custom_response_flask_restful(request, 404, "polleddata chua ton tai", None, None)


        threshold_list_id = polleddata.threshold_lists_id
        threshold_list = session.query(models.Threshold_list).filter_by(id=threshold_list_id).first()
        if threshold_list is None:
            return custom_response_flask_restful(request, 404, "threshold_list chua ton tai", None, None)
        else:
            thresholdobject = session.query(models.Thresholdobject).filter_by(id=data.get('threshold_id'),
                                                                              threshold_lists_id=threshold_list.id).first()
            if thresholdobject is None:
                return custom_response_flask_restful(request, 404, "thresholdobject chua ton tai", None, None)
            else:
                session.delete(thresholdobject)
                session.commit()
        res = models.to_json(threshold_list, 'Threshold_list', False)
        session.close()
        return custom_response_flask_restful(request, 201, None, 'Ok roi nhe, check in http://127.0.0.1:1234/api/v1/threshold_lists/'+ str(threshold_list.id), res)


@namespace.route('/api/get_device_metric', methods=['GET'])
class get_device_metric(Resource):
    @namespace.doc(params={'device_id': "", 'metricid': ""})
    @namespace.response(200, '/api/v1/api/get_device_metric?device_id=xxxx&metricid=yyyy')
    def get(self):
        if not (request.args.get('device_id') or request.args.get('metricid')):
            abort(400)

        data = {'device_id': int(request.args.get('device_id')), 'metricid': int(request.args.get('metricid'))}
        metricdetail = session.query(models.Metricdetail).filter_by(metricid=data.get('metricid')).first()
        if metricdetail is None:
            return custom_response_flask_restful(request, 404, "metricdetail chua ton tai", None, None)

        device = session.query(models.Devicedetail).filter_by(did=data.get('device_id', "")).first()
        if device is None:
            return custom_response_flask_restful(request, 404, "device chua ton tai", None, None)
        polleddata = session.query(models.Polleddata).filter_by(devicedetails_did=device.did, metricdetails_metricid=metricdetail.metricid).first()
        if polleddata is None:
            return custom_response_flask_restful(request, 404, "polleddata chua ton tai", None, None)


        threshold_list_id = polleddata.threshold_lists_id
        threshold_list = session.query(models.Threshold_list).filter_by(id=threshold_list_id).first()
        if threshold_list is None:
            return custom_response_flask_restful(request, 404, "threshold_list chua ton tai", None, None)
        else:
            thresholdobjects = threshold_list.thresholdobjects
            res_json = {
                'metricdetail': models.to_json(metricdetail, 'Metricdetail', False),
                'device': models.to_json(device, 'Devicedetail', False),
                'polleddata': models.to_json(polleddata, 'Polleddata', False),
                'threshold_list': models.to_json(threshold_list, 'Threshold_list', False),
                'thresholdobjects': models.to_json(thresholdobjects, 'Thresholdobject', True)
            }
            session.commit()

        session.close()
        return custom_response_flask_restful(request, 201, None, 'Ok roi nhe', res_json)