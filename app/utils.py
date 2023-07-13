# from passlib.context import CryptContext
# import requests
# import cv2
# import shutil
# import numpy as np


# pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

# def hash(plain_password) :
#     return pwd_context.hash(plain_password)

# def verify_password(plain_password, hashed_password) :
#     return pwd_context.verify(plain_password, hashed_password)



# def send_text(number : str, code : int):
#     message = f"Your verification code is {code}"
#     url = f'''http://66.45.237.70/api.php?username=01782267068&password=6BNPADM4&number={number}&message={message}'''
#     payload  = {}
#     headers = {
#     'Content-Type': 'application/x-www-form-urlencoded'
#     }

#     response = requests.request("POST", url, headers = headers, data = payload)
#     print(response.text.encode('utf8'))


# def mobile_number_verification(mobile_number) :
#     if len(mobile_number) != 11 :
#         return False
#     if mobile_number[:2] != "01" :
#         return False
#     return True


# def write_text_to_image(text):
#     image_path = "bg.jpg"
#     backup_path = f"{text['nid']}.jpg"
#     image = cv2.imread(image_path)
#     cv2.putText(image, "Congratulations!! Here is your vaccination certificate", (500, 500), cv2.QT_FONT_BOLD, 6.0, (0, 255, 0), 10)
#     cv2.imwrite(image_path, image)
#     cv2.putText(image, f"Name : {text['name']}", (500, 900), cv2.QT_FONT_BLACK, 5.0, (0,0, 0), 5)
#     cv2.imwrite(image_path, image)
#     cv2.putText(image, f"NID : {text['nid']}", (500, 1300), cv2.QT_FONT_BLACK, 5.0, (0,0, 0), 5)
#     cv2.imwrite(image_path, image)
#     cv2.putText(image, f"Email : {text['email']}", (500, 1700), cv2.QT_FONT_BLACK, 5.0, (0,0, 0), 5)
#     cv2.imwrite(image_path, image)
#     cv2.putText(image, f"Vaccine taken from :", (500, 2100), cv2.QT_FONT_BLACK, 5.0, (0,0, 0), 5)
#     cv2.imwrite(image_path, image)
#     cv2.putText(image, f"Center : {text['center']}", (500, 2500), cv2.QT_FONT_BLACK, 5.0, (0,0, 0), 5)
#     cv2.imwrite(image_path, image)
#     cv2.putText(image, f"City : {text['city']}", (2500, 2500), cv2.QT_FONT_BLACK, 5.0, (0,0, 0), 5)
#     cv2.imwrite(image_path, image)
#     shutil.copy(image_path, backup_path)
#     image = np.ones(image.shape, dtype=np.uint8) * 255
#     cv2.imwrite(image_path, image)
# # Example usage
