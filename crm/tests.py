# Create your tests here.
import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PerfectCRM.settings")
    import django

    django.setup()

    # t = models.UserProfile.objects.all().first().roles.all().first().menus.all()
    # print(t)

    import json

    t = [{"failed_list": [{"event_time": 1554279180000, "call_back_tag": "bpms_instance_change",
                           "bpms_instance_change": {"corpid": "ding064ce37e8c6fff8435c2f4657eb6378f",
                                                    "bpmsCallBackData": {"createTime": 1554279180000,
                                                                         "title": "\u6881\u660a\u63d0\u4ea4\u7684\u6d41\u91cf\u6c34\u8d28\u76d1\u6d4b\uff08\u5bb9\u5668\u6cd5\uff09",
                                                                         "staffId": "manager405",
                                                                         "processCode": "PROC-ELYJ1A4W-7WJ39FFR3417CDU1EEOZ2-D8YFWXSJ-2",
                                                                         "processInstanceId": "ed421a60-8acd-4680-80b1-ff02719af20e",
                                                                         "bizCategoryId": "",
                                                                         "EventType": "bpms_instance_change",
                                                                         "type": "start",
                                                                         "url": "https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?corpid=ding064ce37e8c6fff8435c2f4657eb6378f&dd_share=false&showmenu=true&dd_progress=false&back=native&procInstId=ed421a60-8acd-4680-80b1-ff02719af20e&taskId=&swfrom=isv&dinghash=approval&dd_from=#approval",
                                                                         "corpId": "ding064ce37e8c6fff8435c2f4657eb6378f"}}},
                          {"event_time": 1554279208000, "call_back_tag": "bpms_instance_change",
                           "bpms_instance_change": {"corpid": "ding064ce37e8c6fff8435c2f4657eb6378f",
                                                    "bpmsCallBackData": {"result": "agree", "createTime": 1554279180000,
                                                                         "title": "\u6881\u660a\u63d0\u4ea4\u7684\u6d41\u91cf\u6c34\u8d28\u76d1\u6d4b\uff08\u5bb9\u5668\u6cd5\uff09",
                                                                         "staffId": "manager405",
                                                                         "processCode": "PROC-ELYJ1A4W-7WJ39FFR3417CDU1EEOZ2-D8YFWXSJ-2",
                                                                         "processInstanceId": "ed421a60-8acd-4680-80b1-ff02719af20e",
                                                                         "bizCategoryId": "",
                                                                         "finishTime": 1554279185000,
                                                                         "EventType": "bpms_instance_change",
                                                                         "type": "finish",
                                                                         "url": "https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?corpid=ding064ce37e8c6fff8435c2f4657eb6378f&dd_share=false&showmenu=true&dd_progress=false&back=native&procInstId=ed421a60-8acd-4680-80b1-ff02719af20e&taskId=&swfrom=isv&dinghash=approval&dd_from=#approval",
                                                                         "corpId": "ding064ce37e8c6fff8435c2f4657eb6378f"}}}],
          "has_more": 'false', "errmsg": "ok", "errcode": 0}]
    print(json.loads(t))
