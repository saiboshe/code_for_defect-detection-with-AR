import os
import json
import xml.etree.ElementTree as ET
from xml.dom import minidom


def convert_labelme_json_to_voc_xml(json_path, output_xml_path):
    """
    将 LabelMe 导出的 JSON 文件转换为符合 VOC 格式的 XML 文件
    参数：
        json_path: LabelMe JSON 文件路径
        output_xml_path: 输出的 VOC 格式 XML 文件路径
    """
    # 读取 JSON 文件
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 创建根节点 <annotation>
    annotation = ET.Element("annotation")

    # 文件夹名称
    folder = ET.SubElement(annotation, "folder")
    folder.text = "VOC2007"

    # 文件名
    filename = ET.SubElement(annotation, "filename")
    filename.text = data.get("imagePath", "unknown.jpg")

    # 图片绝对路径
    path = ET.SubElement(annotation, "path")
    # 这里假设 JSON 中的 imagePath 是图片名，可以结合工作目录得到绝对路径
    path.text = os.path.abspath(data.get("imagePath", "unknown.jpg"))

    # 来源信息
    source = ET.SubElement(annotation, "source")
    database = ET.SubElement(source, "database")
    database.text = "Unknown"

    # 图片尺寸
    size = ET.SubElement(annotation, "size")
    width = ET.SubElement(size, "width")
    width.text = str(data.get("imageWidth", 0))
    height = ET.SubElement(size, "height")
    height.text = str(data.get("imageHeight", 0))
    depth = ET.SubElement(size, "depth")
    depth.text = "3"  # 一般认为是RGB图，所以深度为3

    # segmented
    segmented = ET.SubElement(annotation, "segmented")
    segmented.text = "0"

    # 遍历标注目标
    for shape in data.get("shapes", []):
        # 这里只处理矩形框（shape_type 为 rectangle）
        if shape.get("shape_type", "").lower() != "rectangle":
            continue
        obj = ET.SubElement(annotation, "object")
        name = ET.SubElement(obj, "name")
        name.text = shape.get("label", "undefined")
        pose = ET.SubElement(obj, "pose")
        pose.text = "Unspecified"
        truncated = ET.SubElement(obj, "truncated")
        truncated.text = "0"
        difficult = ET.SubElement(obj, "difficult")
        difficult.text = "0"
        bndbox = ET.SubElement(obj, "bndbox")

        # 读取标注的两个点坐标，计算边界框
        points = shape.get("points", [])
        if len(points) != 2:
            continue  # 如果不是两个点，则跳过
        x1, y1 = points[0]
        x2, y2 = points[1]
        xmin = ET.SubElement(bndbox, "xmin")
        xmin.text = str(int(min(x1, x2)))
        ymin = ET.SubElement(bndbox, "ymin")
        ymin.text = str(int(min(y1, y2)))
        xmax = ET.SubElement(bndbox, "xmax")
        xmax.text = str(int(max(x1, x2)))
        ymax = ET.SubElement(bndbox, "ymax")
        ymax.text = str(int(max(y1, y2)))

    # 使用 minidom 进行格式化输出
    xml_str = ET.tostring(annotation, encoding="utf-8")
    pretty_xml_str = minidom.parseString(xml_str).toprettyxml(indent="    ")

    # 写入 XML 文件
    with open(output_xml_path, "w", encoding="utf-8") as f:
        f.write(pretty_xml_str)
    print(f"转换完成: {json_path} -> {output_xml_path}")


if __name__ == "__main__":
    # 修改以下路径为你的实际路径
    json_directory = "C:/Users/Saber/The University of Manchester Dropbox/Saibo She/real_time_detection/yolov8-pytorch-master/VOCdevkit/VOC2007/json"
    output_xml_directory = "C:/Users/Saber/The University of Manchester Dropbox/Saibo She/real_time_detection/yolov8-pytorch-master/VOCdevkit/VOC2007/xml"

    # 如果输出目录不存在，则创建
    if not os.path.exists(output_xml_directory):
        os.makedirs(output_xml_directory)

    # 遍历json_directory中的所有 JSON 文件进行转换
    for filename in os.listdir(json_directory):
        if filename.lower().endswith(".json"):
            json_path = os.path.join(json_directory, filename)
            xml_filename = os.path.splitext(filename)[0] + ".xml"
            output_xml_path = os.path.join(output_xml_directory, xml_filename)
            convert_labelme_json_to_voc_xml(json_path, output_xml_path)
