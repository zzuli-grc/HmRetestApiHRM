from app import BASE_DIR
import json

login_data_json = BASE_DIR + "/data/login_data.json"
emp_data_json = BASE_DIR + "/data/em_data.json"


# 读取登录数据函数
def read_login():
    with open(login_data_json, mode="r", encoding="utf8") as f:
        data = json.load(f)
        data_list = list()
        for data in data:
            data_tuple = (data.get("mobile"), data.get("password"), data.get("http_code"), data.get("success"),
                          data.get("code"), data.get("message"))
            data_list.append(data_tuple)
    print(data_list)
    return data_list


if __name__ == '__main__':
    read_login()
