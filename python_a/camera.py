import cv2
import os

def main():
    # 打印当前程序自己的PID，Part III作业核心
    my_pid = os.getpid()
    print(f"========== 本程序的PID = {my_pid} ==========")

    # 打开本地摄像头
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("摄像头打开失败！")
        return

    # 获取摄像头分辨率、帧率，用于保存完整视频
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 创建视频写入器：只保存【原始彩色画面】
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter("raw_capture.mp4", fourcc, fps, (width, height))

    # 主循环
    while True:
        # 读取原始帧
        ret, frame = cap.read()
        if not ret:
            break

        # 1. 原始彩色图像
        img_original = frame

        # 2. 灰度图像
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 3. 轮廓处理图像
        _, binary = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        img_contour = frame.copy()
        cv2.drawContours(img_contour, contours, -1, (0, 255, 0), 2)

        # 打开三个独立窗口（作业要求截图三窗口同时存在）
        cv2.imshow("1_原始图像", img_original)
        cv2.imshow("2_灰度图像", img_gray)
        cv2.imshow("3_轮廓处理图像", img_contour)

        # 写入原始画面（绝对不写灰度图，防止扣分）
        video_writer.write(img_original)

        # 按键退出：q键 / ESC键
        key = cv2.waitKey(1)
        if key == ord("q") or key == 27:
            break

    # 必须释放资源（否则视频损坏打不开）
    video_writer.release()
    cap.release()
    cv2.destroyAllWindows()
    print("程序结束，原始视频 raw_capture.mp4 保存成功！")

if __name__ == "__main__":
    main()
