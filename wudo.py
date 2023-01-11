# pip install wudao 请先在终端进行安装，或者到开放平台用户手册中--》》新手指南下载平台调用工具包。
# -*- coding:utf-8 -*-
from wudao.api_request import executeEngineV2, getToken,queryTaskResult
import random
def Submitwudao(content):
    # 接口API KEY
    API_KEY = "4c86badf3bc446319cffa2d8d11c1925"
    # 公钥
    PUBLIC_KEY = "MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBALZ0v4NUxbXIvqwSzJybHM0cg/GenGJ2ryPhn7NiW7HBs7u25v5UFTR9ubHaXerPSPuK9sHA6KLiM4h35a3sJH8CAwEAAQ=="
    # 能力类型
    ability_type = "question_answer"
    # 引擎类型
    engine_type = "txl-general-engine-v1"
    requestTaskNo=str(random.randint(1542097269879345196,1542097269879345196*6))
    # 请求参数样例
    data = {
        "topP": 1,
        "topK": 3,
        "temperature": 1,
        "presencePenalty": 1,
        "frequencyPenalty": 1,
        "generatedLength": 128,
        "prompt": content,
        "promptDesc": "哲学",
        "requestTaskNo": requestTaskNo
    }

    '''
    注意这里仅为了简化编码每一次请求都去获取token， 线上环境token有过期时间， 客户端可自行缓存，过期后重新获取。
    '''
    token_result = getToken(API_KEY, PUBLIC_KEY)

    if token_result and token_result["code"] == 200:
        token = token_result["data"]
        resp = executeEngineV2(ability_type, engine_type, token, data)
        if resp["success"] ==True:
            while True:
                resp1 = queryTaskResult(token, resp["data"]["taskOrderNo"])
                if resp1['data']['outputText'] is not None:
                    print("resp1:",resp1)
                    break
            return resp1['data']['outputText']
        else:
            print("queryTaskResult,False")
        
    else:
        print("获取token失败，请检查 API_KEY 和 PUBLIC_KEY")
