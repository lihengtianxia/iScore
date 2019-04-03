from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '15871401'
API_KEY = 'syh6PAMcs0No4LkMMxsL39n1'
SECRET_KEY = 'oZ9UIv5TQ8augjrQGIObTU2aceAqxRuR'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content('timg1.jpg')

""" 调用银行卡识别 """
res = client.bankcard(image)

print(res)