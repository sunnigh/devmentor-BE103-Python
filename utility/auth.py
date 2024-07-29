from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    """
    將密碼hash加密
    :param password:
    :return:
    """
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    """
    驗證密碼
    :param plain_password:
    :param hashed_password:
    :return:
    """
    return pwd_context.verify(plain_password, hashed_password)







