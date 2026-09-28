import argparse
import imageio
import numpy as np
from skimage.color import rgb2gray
from skimage.feature import canny


def main():
    # 解析命令行参数，完全匹配作业运行调用格式
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True, help="输入视频路径，一般为 ../python_A/raw_capture.mp4")
    parser.add_argument("--output", type=str, required=True, help="输出视频路径")
    args = parser.parse_args()

    # 打开读取视频
    reader = imageio.get_reader(args.input)
    meta = reader.get_meta_data()
    fps = meta["fps"]

    writer = imageio.get_writer(args.output, fps=fps)

    prev_gray = None

    for frame_rgb in reader:
        # --------------------画面1：原始图像（RGB原图）--------------------
        frame_original = frame_rgb

        # --------------------画面2：Canny边缘检测（skimage自带，不用OpenCV）--------------------
        gray = rgb2gray(frame_rgb)
        canny_edge_float = canny(gray, sigma=1.2)
        canny_edge_uint8 = (canny_edge_float * 255).astype(np.uint8)
        # 扩展为三通道，用来拼接画面
        frame_canny = np.stack([canny_edge_uint8, canny_edge_uint8, canny_edge_uint8], axis=-1)

        # --------------------画面3：帧间运动区域，前后帧做差值得到运动变化---------------------
        if prev_gray is None:
            motion_mask = np.zeros_like(gray)
        else:
            frame_diff = np.abs(gray - prev_gray)
            # 阈值筛选，把变化大的像素标记为运动区域
            motion_mask = np.where(frame_diff > 0.06, 1.0, 0.0)
        motion_uint8 = (motion_mask * 255).astype(np.uint8)
        frame_motion = np.stack([motion_uint8, motion_uint8, motion_uint8], axis=-1)

        # 更新上一帧灰度图，用于下一回合帧差计算
        prev_gray = gray.copy()

        # 将三张图像横向拼接到一起：【原图 ‖ Canny边缘 ‖帧间运动区域】
        combined_frame = np.hstack([frame_original, frame_canny, frame_motion])

        writer.append_data(combined_frame)

    writer.close()
    reader.close()
    print(f"✅处理完成！输出文件保存在：{args.output}")


if __name__ == "__main__":
    main()
