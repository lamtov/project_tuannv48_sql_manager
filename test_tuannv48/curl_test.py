import os
import time
import requests

my_api_host_ip = "127.0.0.1:1234"


###*******************************add_host_to_role *******************************************************
def add_devicedetails():
    payloads = [
        {"mode": "controller87_disk_sda", "status": "created", "errorstring": "no", "isprofilebased": 0,
         "fetch_rules": 0, "ip": "172.16.30.87"},
        {"mode": "controller87_disk_dm-1", "status": "created", "errorstring": "no", "isprofilebased": 0,
         "fetch_rules": 0, "ip": "172.16.30.87"},
        {"mode": "controller87_vnic_p1p2", "status": "created", "errorstring": "no", "isprofilebased": 0,
         "fetch_rules": 0, "ip": "172.16.30.87"},
        {"mode": "controller87_vnic_em1", "status": "created", "errorstring": "no", "isprofilebased": 0,
         "fetch_rules": 0, "ip": "172.16.30.87"}
    ]
    for i in range(0, 4):
        url = 'http://' + str(my_api_host_ip) + '/api/v1/insert/add_devicedetails'
        payload = payloads[i]
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.post(url, json=payload, headers=headers)
        print(r.text)
        time.sleep(5)


def add_protocoldetails():
    payloads = [
        {"protocolname": "collectd"},
        {"protocolname": "collectd2"}]
    for i in range(0, 2):
        url = 'http://' + str(my_api_host_ip) + '/api/v1/insert/add_protocoldetails'
        payload = payloads[i]
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.post(url, json=payload, headers=headers)
        print(r.text)
        time.sleep(5)


def add_metricdetails():
    payloads = [
        {"metricname": "diskOpsWriteLast", "description": "diskOpsWriteLast", "displayname": "diskOpsWriteLast",
         "metrictype": 1, "datatype": 1, "protocolid": 2},
        {"metricname": "diskMergedWriteLast", "description": "diskMergedWriteLast",
         "displayname": "diskMergedWriteLast", "metrictype": 1, "datatype": 1, "protocolid": 2},
        {"metricname": "diskOctetsWriteLast", "description": "diskOctetsWriteLast",
         "displayname": "diskOctetsWriteLast", "metrictype": 1, "datatype": 1, "protocolid": 2},
        {"metricname": "receivedOctetsAccumulated", "description": "receivedOctetsAccumulated",
         "displayname": "receivedOctetsAccumulated", "metrictype": 1, "datatype": 1, "protocolid": 2},
        {"metricname": "transmittedTotalPacketsAccumulated", "description": "transmittedTotalPacketsAccumulated",
         "displayname": "transmittedTotalPacketsAccumulated", "metrictype": 1, "datatype": 1, "protocolid": 2},
        {"metricname": "transmittedOctetsAccumulated", "description": "transmittedOctetsAccumulated",
         "displayname": "transmittedOctetsAccumulated", "metrictype": 1, "datatype": 1, "protocolid": 2},

    ]
    for i in range(0, 5):
        url = 'http://' + str(my_api_host_ip) + '/api/v1/insert/add_metricdetails'
        payload = payloads[i]
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.post(url, json=payload, headers=headers)
        print(r.text)
        time.sleep(5)


def add_threshold_lists():
    payloads = [
        {"description": "lnMemFree"},
        {"description": "diskMergedWriteLast"},
        {"description": "diskOctetsWriteLast"},
        {"description": "diskOpsWriteLast"},
        {"description": "diskMergedWriteLast"},
        {"description": "receivedOctetsAccumulated"},
        {"description": "transmittedTotalPacketsAccumulated"},
        {"description": "diskOpsWriteLast"},
        {"description": "transmittedOctetsAccumulated"}
    ]
    for i in range(2, 8):
        url = 'http://' + str(my_api_host_ip) + '/api/v1/insert/add_threshold_lists'
        payload = payloads[i]
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.post(url, json=payload, headers=headers)
        print(r.text)
        time.sleep(5)


def add_thresholdobjects():
    payloads = [
        {'name': 'lnMemFree', 'kind': 'long', 'priority': 4, 'category': 'Threshold', 'thresholdvalue': 25,
         'rearmvalue': 200,
         'mmessage': '$MONITOR for $INSTANCE is $CURRENTVALUE $UNITS threshold value for this monitor is $THRESHOLDVALUE $UNITS',
         'allowed': 1, 'is_customize': 0, 'consecutive_time': 3, 'threshold_lists_id': 4},
        {'name': 'lnMemFree', 'kind': 'long', 'priority': 3, 'category': 'Threshold', 'thresholdvalue': 50,
         'rearmvalue': 200,
         'mmessage': '$MONITOR for $INSTANCE is $CURRENTVALUE $UNITS threshold value for this monitor is $THRESHOLDVALUE $UNITS',
         'allowed': 1, 'is_customize': 0, 'consecutive_time': 3, 'threshold_lists_id': 4},
        {'name': 'lnMemFree', 'kind': 'long', 'priority': 2, 'category': 'Threshold',
         'thresholdvalue': 100, 'rearmvalue': 200,
         'mmessage': '$MONITOR for $INSTANCE is $CURRENTVALUE $UNITS threshold value for this monitor is $THRESHOLDVALUE $UNITS',
         'allowed': 1, 'is_customize': 0,
         'consecutive_time': 3,
         'threshold_lists_id': 4},
        {'name': 'lnMemFree', 'kind': 'long', 'priority': 1, 'category': 'Threshold',
         'thresholdvalue': 150, 'rearmvalue': 200,
         'mmessage': '$MONITOR for $INSTANCE is $CURRENTVALUE $UNITS threshold value for this monitor is $THRESHOLDVALUE $UNITS',
         'allowed': 1, 'is_customize': 0,
         'consecutive_time': 3,
         'threshold_lists_id': 4}

    ]
    for i in range(0, 4):
        url = 'http://' + str(my_api_host_ip) + '/api/v1/insert/add_thresholdobjects'
        payload = payloads[i]
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.post(url, json=payload, headers=headers)
        print(r.text)
        time.sleep(5)

def add_groupdevices():
    payloads = [
        {'group_name':"group1", 'group_desc': "des1",'is_manual':True},
        {"group_name":"group2", 'group_desc':"des2",'is_manual':True}]
    for i in range(0, 2):
        url = 'http://' + str(my_api_host_ip) + '/api/v1/insert/add_groupdevices'
        payload = payloads[i]
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.post(url, json=payload, headers=headers)
        print(r.text)
        time.sleep(5)



def add_polleddata():
    payloads = [
        {'name': 'test2',
         'period': 50, 'active': 1, 'threshold_activate': 1,
         'devicedetails_did': 16,
         'groupdevices_group_id': 3,
         'threshold_lists_id': 4,
         'metricdetails_metricid': 9},
        {'name': 'test3',
         'period': 50, 'active': 1, 'threshold_activate': 1,
         'devicedetails_did': 16,
         'groupdevices_group_id': 3,
         'threshold_lists_id': 5,
         'metricdetails_metricid': 10},
        {'name': 'test4',
         'period': 50, 'active': 1, 'threshold_activate': 1,
         'devicedetails_did': 17,
         'groupdevices_group_id': 3,
         'threshold_lists_id': 3,
         'metricdetails_metricid': 11},
        {'name': 'test5',
         'period': 50, 'active': 1, 'threshold_activate': 1,
         'devicedetails_did': 17,
         'groupdevices_group_id': 3,
         'threshold_lists_id': 4,
         'metricdetails_metricid': 12},
        {'name': 'test6',
         'period': 50, 'active': 1, 'threshold_activate': 1,
         'devicedetails_did': 18,
         'groupdevices_group_id': 3,
         'threshold_lists_id': 6,
         'metricdetails_metricid': 13},
        {'name': 'test7',
         'period': 50, 'active': 1, 'threshold_activate': 1,
         'devicedetails_did': 18,
         'groupdevices_group_id': 1,
         'threshold_lists_id': 7,
         'metricdetails_metricid': 13},
        {'name': 'test8',
         'period': 50, 'active': 1, 'threshold_activate': 1,
         'devicedetails_did': 19,
         'groupdevices_group_id': 3,
         'threshold_lists_id': 8,
         'metricdetails_metricid': 13},
        {'name': 'test9',
         'period': 50, 'active': 1, 'threshold_activate': 1,
         'devicedetails_did': 19,
         'groupdevices_group_id': 3,
         'threshold_lists_id': 7,
         'metricdetails_metricid': 13}
    ]
    for i in range(0, 8):
        url = 'http://' + str(my_api_host_ip) + '/api/v1/insert/add_protocoldetails'
        payload = payloads[i]
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.post(url, json=payload, headers=headers)
        print(r.text)
        time.sleep(5)







# def add_alert():
#     payloads = [
#         {"protocolname": "collectd"},
#         {"protocolname": "collectd2"}]
#     for i in range(0, 2):
#         url = 'http://' + str(my_api_host_ip) + '/api/v1/insert/add_protocoldetails'
#         payload = payloads[i]
#         headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
#         r = requests.post(url, json=payload, headers=headers)
#         print(r.text)
#         time.sleep(5)
#
#
# def add_groupalerts():
#     payloads = [
#         {"protocolname": "collectd"},
#         {"protocolname": "collectd2"}]
#     for i in range(0, 2):
#         url = 'http://' + str(my_api_host_ip) + '/api/v1/insert/add_protocoldetails'
#         payload = payloads[i]
#         headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
#         r = requests.post(url, json=payload, headers=headers)
#         print(r.text)
#         time.sleep(5)
#
#
# def add_groupdevicepolledatatemplate():
#     payloads = [
#         {"protocolname": "collectd"},
#         {"protocolname": "collectd2"}]
#     for i in range(0, 2):
#         url = 'http://' + str(my_api_host_ip) + '/api/v1/insert/add_protocoldetails'
#         payload = payloads[i]
#         headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
#         r = requests.post(url, json=payload, headers=headers)
#         print(r.text)
#         time.sleep(5)
#
#
# def add_groupdevicesdevicedetails():
#     payloads = [
#         {"protocolname": "collectd"},
#         {"protocolname": "collectd2"}]
#     for i in range(0, 2):
#         url = 'http://' + str(my_api_host_ip) + '/api/v1/insert/add_protocoldetails'
#         payload = payloads[i]
#         headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
#         r = requests.post(url, json=payload, headers=headers)
#         print(r.text)
#         time.sleep(5)
#
#
# def add_metricdetails():
#     payloads = [
#         {"protocolname": "collectd"},
#         {"protocolname": "collectd2"}]
#     for i in range(0, 2):
#         url = 'http://' + str(my_api_host_ip) + '/api/v1/insert/add_protocoldetails'
#         payload = payloads[i]
#         headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
#         r = requests.post(url, json=payload, headers=headers)
#         print(r.text)
#         time.sleep(5)
#
#
# def add_polldatatemplate():
#     payloads = [
#         {"protocolname": "collectd"},
#         {"protocolname": "collectd2"}]
#     for i in range(0, 2):
#         url = 'http://' + str(my_api_host_ip) + '/api/v1/insert/add_protocoldetails'
#         payload = payloads[i]
#         headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
#         r = requests.post(url, json=payload, headers=headers)
#         print(r.text)
#         time.sleep(5)
def create_template():
    payloads = [
        {'group_name': "fields.String", 'group_desc': "fields.String",
         'metricid': 12, 'threshold_value_1': 2,
         'threshold_value_2': 4, 'threshold_value_3': 7,
         'threshold_value_4': 9, 'rearmvalue': 50}

    ]
    for i in range(0, 1):
        url = 'http://' + str(my_api_host_ip) + '/api/v1/api/create_template'
        payload = payloads[i]
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.post(url, json=payload, headers=headers)
        print(r.text)
        time.sleep(5)
def add_threshold_to_template():
    payloads = [
        {'group_id':3,
         'metricid': 12, 'threshold_value_1': 20,
         'threshold_value_2': 10, 'threshold_value_3': 20,
         'threshold_value_4': 30, 'rearmvalue': 40}

    ]
    for i in range(0, 1):
        url = 'http://' + str(my_api_host_ip) + '/api/v1/api/add_threshold_to_template'
        payload = payloads[i]
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.post(url, json=payload, headers=headers)
        print(r.text)
        time.sleep(5)
def update_threshold_in_template():
    payloads = [
        {'group_id': 3,
         'metricid': 12, 'threshold_value_1': 200,
         'threshold_value_2': 100, 'threshold_value_3': 200,
         'threshold_value_4': 300, 'rearmvalue': 400}

    ]
    for i in range(0, 1):
        url = 'http://' + str(my_api_host_ip) + '/api/v1/api/update_threshold_in_template'
        payload = payloads[i]
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.post(url, json=payload, headers=headers)
        print(r.text)
        time.sleep(5)
def delete_threshold_in_template():
    payloads = [
        {'group_id': 3,
         'metricid': 12, 'threshold_id': 14}

    ]
    for i in range(0, 1):
        url = 'http://' + str(my_api_host_ip) + '/api/v1/api/delete_threshold_in_template'
        payload = payloads[i]
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.post(url, json=payload, headers=headers)
        print(r.text)
        time.sleep(5)


def create_threshold():
    payloads = [
        {'device_name': "fields.String", 'device_ip': "fields.String",
         'metricid': 12, 'threshold_value_1': 2,
         'threshold_value_2': 4, 'threshold_value_3': 7,
         'threshold_value_4': 9, 'rearmvalue': 50}

    ]
    for i in range(0, 1):
        url = 'http://' + str(my_api_host_ip) + '/api/v1/api/create_threshold'
        payload = payloads[i]
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.post(url, json=payload, headers=headers)
        print(r.text)
        time.sleep(5)
def add_threshold_to_device():
    payloads = [
        {'device_id':16,
         'metricid': 12, 'threshold_value_1': 9,
         'threshold_value_2': 10, 'threshold_value_3': 11,
         'threshold_value_4': 12, 'rearmvalue': 50}

    ]
    for i in range(0, 1):
        url = 'http://' + str(my_api_host_ip) + '/api/v1/api/add_threshold_to_device'
        payload = payloads[i]
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.post(url, json=payload, headers=headers)
        print(r.text)
        time.sleep(5)
def update_threshold_to_device():
    payloads = [
        {'device_id': 16,
         'metricid': 12, 'threshold_value_1': 13,
         'threshold_value_2': 14, 'threshold_value_3': 11,
         'threshold_value_4': 12, 'rearmvalue': 50}

    ]
    for i in range(0, 1):
        url = 'http://' + str(my_api_host_ip) + '/api/v1/api/update_threshold_to_device'
        payload = payloads[i]
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.post(url, json=payload, headers=headers)
        print(r.text)
        time.sleep(5)
def delete_threshold_in_device():
    payloads = [
        {'device_id': 16,
         'metricid': 12, 'threshold_id': 27}

    ]
    for i in range(0, 1):
        url = 'http://' + str(my_api_host_ip) + '/api/v1/api/delete_threshold_in_device'
        payload = payloads[i]
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.post(url, json=payload, headers=headers)
        print(r.text)
        time.sleep(5)

if __name__ == "__main__":
    # add_devicedetails()
    # add_protocoldetails()
    # add_metricdetails()
    # add_threshold_lists()
    # add_thresholdobjects()
    # add_groupdevices()
    # add_polleddata()
    # create_template()
    # add_threshold_to_template()
    # update_threshold_in_template()
    # delete_threshold_in_template()
    # create_threshold()
    # add_threshold_to_device()
    # update_threshold_to_device()
    delete_threshold_in_device()