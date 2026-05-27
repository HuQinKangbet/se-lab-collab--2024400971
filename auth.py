def user_authenticate(username, password):
    """
    用户登录验证函数
    :param username: 用户名
    :param password: 密码
    :return: str 登录结果（登录成功/登录失败）
    """
    if username == "admin" and password == "123456":
        return "登录成功"
    else:
        return "登录失败"