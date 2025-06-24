Training Steps
a. Training on the VOC07+12 Dataset
Dataset Preparation
This project uses the VOC format for training. Before training, download the VOC07+12 dataset and extract it into the root directory.

Dataset Processing
Set annotation_mode=2 in voc_annotation.py, then run voc_annotation.py to generate 2007_train.txt and 2007_val.txt in the root directory.

Start Network Training
The default parameters in train.py are for training on the VOC dataset. Simply run train.py to begin training.

Prediction with Trained Model
Prediction requires two files: yolo.py and predict.py. First, modify model_path and classes_path in yolo.py. These two parameters must be changed:

model_path: Path to the trained weights file (located in the logs folder).

classes_path: Path to the .txt file listing detection classes.
After modifying, run predict.py and input the image path to perform detection.

b. Training on a Custom Dataset
Dataset Preparation
This project uses the VOC format for training. Before training, you need to prepare your own dataset.

Place annotation files in VOCdevkit/VOC2007/Annotations

Place image files in VOCdevkit/VOC2007/JPEGImages

Dataset Processing
After placing the dataset files, run voc_annotation.py to generate 2007_train.txt and 2007_val.txt.
Initially, only modify the classes_path in voc_annotation.py. It should point to a .txt file that lists your custom classes (e.g., model_data/cls_classes.txt):

cat  
dog  
...  
Set classes_path in voc_annotation.py to this file, then run the script.

Start Network Training
Training parameters are defined in train.py. Read the comments in the file carefully.
The most important setting is classes_path, which must be changed to match the one used in voc_annotation.py!
After modifying it, run train.py to begin training. Trained weights will be saved in the logs folder.

Prediction with Trained Model
Prediction requires yolo.py and predict.py. Modify model_path and classes_path in yolo.py:

model_path: Path to your trained weights (in the logs folder)

classes_path: Path to your class list .txt file
Then run predict.py and input an image path for detection.

Inference Steps
a. Using Pre-trained Weights
After downloading and extracting the repo, download the pretrained weights via Baidu Drive and place them in the model_data folder. Run predict.py and input:

img/street.jpg  
predict.py can be modified for FPS testing and video detection.

b. Using Your Own Trained Weights
Train the model as described above.

In yolo.py, modify model_path and classes_path to point to your trained weights and class file:

_defaults = {
    # Use your own trained model — modify model_path and classes_path!
    # model_path: path to trained weights in logs folder
    # classes_path: path to corresponding class list in model_data

    "model_path": 'model_data/yolov8_s.pth',
    "classes_path": 'model_data/coco_classes.txt',

    "anchors_path": 'model_data/yolo_anchors.txt',
    "anchors_mask": [[6, 7, 8], [3, 4, 5], [0, 1, 2]],
    "input_shape": [640, 640],

    "phi": 's',
    "confidence": 0.5,
    "nms_iou": 0.3,
    "letterbox_image": True,
    "cuda": True,
}
Run predict.py and input:


img/street.jpg  
In predict.py, you can enable FPS testing and video detection.


Evaluation Steps
a. Evaluate on VOC07+12 Test Set
This project uses VOC format for evaluation. VOC07+12 already includes a test split, so you don’t need to generate .txt files in the ImageSets folder using voc_annotation.py.

Modify model_path and classes_path in yolo.py:

model_path: Trained weights in logs folder

classes_path: Path to class list .txt file

Run get_map.py to generate evaluation results. Output will be saved in the map_out folder.

b. Evaluate on Your Own Dataset
This project uses VOC format for evaluation.

If voc_annotation.py has been run before training, the dataset will already be split into training, validation, and test sets. To adjust the test ratio, modify trainval_percent in voc_annotation.py.

trainval_percent: Ratio of (train + val) to test (default: 9:1)

train_percent: Ratio of train to val within (train + val) (default: 9:1)

After generating test set splits, modify classes_path in get_map.py to match the .txt file used during training. This must be updated for custom datasets.

Modify model_path and classes_path in yolo.py to match your trained model.

Run get_map.py to get evaluation results (saved in map_out).

Reference
https://github.com/ultralytics/ultralytics

Let me know if you'd like the translated text formatted as a Markdown document or a PDF file