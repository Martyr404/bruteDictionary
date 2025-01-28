import os
import zipfile

def unzip_with_password_dict(zip_path, password_dict_path):
    """
    使用密码字典尝试解压带密码的压缩包
    :param zip_path: 压缩包路径
    :param password_dict_path: 密码字典文件路径
    """
    # 检查压缩包是否存在
    if not os.path.exists(zip_path):
        print(f"压缩包不存在: {zip_path}")
        return

    # 检查密码字典是否存在
    if not os.path.exists(password_dict_path):
        print(f"密码字典不存在: {password_dict_path}")
        return

    # 打开压缩包
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # 读取密码字典
        with open(password_dict_path, 'r', encoding='utf-8') as f:
            for line in f:
                password = line.strip()  # 去除换行符和空白字符
                if not password:  # 跳过空行
                    continue
                try:
                    # 尝试用当前密码解压
                    zip_ref.extractall(pwd=password.encode('utf-8'))
                    print(f"解压成功！密码为: {password}")
                    return  # 解压成功后退出
                except RuntimeError as e:
                    if 'password' in str(e).lower():
                        # 密码错误，继续尝试下一个
                        continue
                    else:
                        # 其他错误（如文件损坏）
                        print(f"解压失败: {e}")
                        return
                except zipfile.BadZipFile:
                    print(f"文件损坏或不是有效的zip文件: {zip_path}")
                    return

    # 如果所有密码都尝试失败
    print("解压失败：密码字典中没有正确的密码。")

# 压缩包路径
zip_path = "./131911.zip"

# 密码字典路径
password_dict_path = "./keyboard_top500.txt"

# 尝试解压
unzip_with_password_dict(zip_path, password_dict_path)



# 调用函数解压文件
# unzip_files_in_directory(target_directory, zip_password)