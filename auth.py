def user_login(username, password):
    """
    用户登录功能
    :param username: 用户名
    :param password: 密码
    :return: 登录成功/失败
    """
    if username == "admin" and password == "123456":
        return "登录成功"
    else:
        return "登录失败"