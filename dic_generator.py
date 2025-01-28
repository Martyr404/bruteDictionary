import itertools
def generate_password_dict(output_file, min_length=1, max_length=6, chars=None):
    """
    生成密码字典并保存到文件
    :param output_file: 输出文件路径
    :param min_length: 密码最小长度
    :param max_length: 密码最大长度
    :param chars: 密码字符集，默认为小写字母和数字
    """
    if chars is None:
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"  # 默认字符集

    with open(output_file, 'w') as f:
        # 遍历所有可能的长度
        for length in range(min_length, max_length + 1):
            # 使用 itertools.product 生成所有可能的组合
            for combination in itertools.product(chars, repeat=length):
                password = ''.join(combination)  # 将元组转换为字符串
                f.write(password + '\n')  # 写入文件

    print(f"密码字典已生成并保存到: {output_file}")


output_file = "password_dict.txt"


generate_password_dict(output_file, min_length=1, max_length=6)