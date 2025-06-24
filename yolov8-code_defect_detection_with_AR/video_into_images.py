import cv2
import os


def extract_frames(video_path, output_folder):
    # 如果输出文件夹不存在则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 打开视频文件
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"无法打开视频文件：{video_path}")
        return

    frame_index = 200  # 视频中当前帧的索引
    saved_frame_count = 0  # 保存的帧计数器

    while True:
        ret, frame = cap.read()
        # 如果读取失败则退出循环
        if not ret:
            break

        # 每10帧抽取一帧（例如第0帧、第10帧、第20帧...）
        if frame_index % 10 == 0:
            # 构造每一帧的保存路径，文件名带有帧编号
            frame_filename = os.path.join(output_folder, f"frame_{saved_frame_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            saved_frame_count += 1

        frame_index += 1

    cap.release()
    print(f"视频总帧数：{frame_index}，共保存帧数：{saved_frame_count}")


if __name__ == '__main__':
    # 视频文件路径
    video_path = 'C:/Users/Saber/Desktop/1(1).avi'
    # 输出文件夹
    output_folder = 'frames'
    extract_frames(video_path, output_folder)
