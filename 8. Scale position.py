import pyautogui

def scale_position(x, y, source_resolution, target_resolution):
    source_width, source_height = source_resolution
    target_width, target_height = target_resolution
    
    scaled_x = (x / source_width) * target_width
    scaled_y = (y / source_height) * target_height
    
    return int(scaled_x), int(scaled_y)

def main():
    # Độ phân giải của màn hình lớn (ví dụ: 3000x455)
    source_resolution = (3000, 455)
    
    # Tọa độ x, y trên màn hình lớn
    x = 555
    y = 120
    
    # Lấy độ phân giải của màn hình hiện tại
    target_width, target_height = pyautogui.size()
    target_resolution = (target_width, target_height)
    
    # Tính toán tọa độ trên màn hình hiện tại
    scaled_x, scaled_y = scale_position(x, y, source_resolution, target_resolution)
    
    print(f"Tọa độ tương ứng trên màn hình hiện tại: x = {scaled_x}, y = {scaled_y}")

if __name__ == "__main__":
    main()
