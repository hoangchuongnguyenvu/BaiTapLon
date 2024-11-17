import cv2
import numpy as np

def load_image(uploaded_file):
    # Hàm load và xử lý ảnh dùng chung
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    return cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

# Thêm các hàm tiện ích khác