import os
import random


def split_dataset(image_dir, output_dir, train_ratio=0.6, val_ratio=0.2, test_ratio=0.2, seed=42):
    """
    从 image_dir 文件夹中读取图片名称，随机划分为 train、val、test 三个集合，
    同时生成 trainval（train+val）集合，并将四个集合的名称写入各自的 txt 文件中。

    参数：
        image_dir: 存放图片的文件夹路径
        output_dir: 输出 txt 文件的文件夹路径
        train_ratio: 训练集比例（默认 0.6）
        val_ratio: 验证集比例（默认 0.2）
        test_ratio: 测试集比例（默认 0.2）
        seed: 随机种子（保证每次划分一致）
    """
    # 检查比例和是否为1
    total_ratio = train_ratio + val_ratio + test_ratio
    if abs(total_ratio - 1.0) > 1e-6:
        raise ValueError("train_ratio, val_ratio, test_ratio 的和必须为 1")

    # 定义支持的图片后缀
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']

    # 获取所有图片文件
    images = [f for f in os.listdir(image_dir) if os.path.splitext(f)[1].lower() in image_extensions]

    if len(images) == 0:
        print("未找到图片，请检查图片文件夹路径和图片格式。")
        return

    # 设置随机种子，并打乱列表
    random.seed(seed)
    random.shuffle(images)

    total_num = len(images)
    train_end = int(total_num * train_ratio)
    val_end = train_end + int(total_num * val_ratio)

    # 划分数据集
    train_list = images[:train_end]
    val_list = images[train_end:val_end]
    test_list = images[val_end:]
    trainval_list = train_list + val_list  # trainval 为 train 与 val 的合并

    # 如果输出目录不存在则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

        # 写入 txt 文件的函数（去除文件后缀）

    def write_list(file_path, data_list):
        with open(file_path, 'w', encoding='utf-8') as f:
            for item in data_list:
                name_without_ext = os.path.splitext(item.strip())[0]
                f.write(name_without_ext + "\n")

        # 写入各个 txt 文件

    write_list(os.path.join(output_dir, 'train.txt'), train_list)
    write_list(os.path.join(output_dir, 'val.txt'), val_list)
    write_list(os.path.join(output_dir, 'test.txt'), test_list)
    write_list(os.path.join(output_dir, 'trainval.txt'), trainval_list)

    print(f"总图片数: {total_num}")
    print(
        f"train: {len(train_list)}  |  val: {len(val_list)}  |  test: {len(test_list)}  |  trainval: {len(trainval_list)}")


if __name__ == '__main__':
    # 修改为你的图片文件夹路径
    image_dir = "C:/Users/Saber/Desktop/yolov8-pytorch-master/yolov8-pytorch-master/data_for_ARdefect/data"
    # 修改为你想保存 txt 文件的输出目录
    output_dir = "C:/Users/Saber/Desktop/yolov8-pytorch-master/yolov8-pytorch-master/data_for_ARdefect/data"
    split_dataset(image_dir, output_dir)
