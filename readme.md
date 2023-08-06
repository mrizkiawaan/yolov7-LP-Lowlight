# YOLOv7-LP-Lowlight

implementation and documentation of the final project entitled **"Identification of Vehicle License Plates in Low Light Conditions Using the YOLOv7 and OCR Methods"**

### Setup for YOLOv7 in Google Colab

1. Create google colab file and connect to google drive
2. Set the runtime to GPU. **Runtime > Change runtime type > GPU**
3. Clone [Official YOLOv7 Repository](https://github.com/WongKinYiu/yolov7.git)
4. Download [pre-trained YOLOv7 Weight](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt)
5. Install requirements with `!pip install -r requirements.txt`
6. Upload `dataset` to `yolov7\data` in cloned repository at google drive

Link to colab [here](https://colab.research.google.com/drive/1tvsmf3IjFXlsXIwM30MKdlVGCo_qJlLB?usp=sharing)

[Sample cloned repository in google drive](https://drive.google.com/drive/folders/1eYjaeslBM8M8RaoXAGwr_e5gHylmJXTv?usp=sharing)

### Editing config file

1.  Open `yolov7/data/coco.yaml` and delete the first 4 lines (till the download part).
2.  Change the code in the file as follows

```
train: data/dataset/train/License Plate
val: data/dataset/val/License Plate
test: data/dataset/test/License Plate

# number of classes
nc:  1

# class names
names:  ['License Plate']
```

3. Open `yolov7\cfg\training\yolov7.yaml` and change the nc (no of class) in line 2 with value 1 `nc: 1  # number of classes`

\*Note that google drive doesn't have text editor to edit the file, you have to do this in local environment with your own text editor and replace `coco.yaml` and `yolov7.yaml` in cloned repository at google drive

### YOLOv7 Training and testing

You can follow command in [YOLOv7 Official Repository](https://github.com/WongKinYiu/yolov7)
**Training**

```
# train p5 models
# finetune p5 models
python train.py --workers 8 --device 0 --batch-size 32 --data data/custom.yaml --img 640 640 --cfg cfg/training/yolov7-custom.yaml --weights 'yolov7_training.pt' --name yolov7-custom --hyp data/hyp.scratch.custom.yaml

# finetune p6 models
python train_aux.py --workers 8 --device 0 --batch-size 16 --data data/custom.yaml --img 1280 1280 --cfg cfg/training/yolov7-w6-custom.yaml --weights 'yolov7-w6_training.pt' --name yolov7-w6-custom --hyp data/hyp.scratch.custom.yaml
```

**Testing**

```
python test.py --data data/coco.yaml --img 640 --batch 32 --conf 0.001 --iou 0.65 --device 0 --weights yolov7.pt --name yolov7_640_val
```

### Running OCR

1. Install easyocr, kerasocr, and pytesseract module with `pip install keras-ocr easyocr pytesseract`
2. Clone [YOLOv7-object-cropping](https://github.com/RizwanMunawar/yolov7-object-cropping.git) repository to crop YOLOv7 detection result.
3. Download weight from your training result and save in YOLOv7-object-cropping folder. Your training weight will be at `yolov7\runs\train\yolov7-custom\weights\best.pt` in google drive.
4. Copy `Dataset\Split\test` to `yolov7-object-cropping`
5. Run detect and crop with this following command

```
python detect_and_crop.py --weights best.pt --source "\test\License Plate"
```

\*adjust source to your folder path, if it doesn't work use full path.
The result will be at `yolov7-object-cropping\crop` 

6. Adjust ground truth and image file at `ocr_accuracy.py` according to image folder in previous step.
7. Run `ocr_accuracy.py` with vscode.

### Reference

- [YOLOv7 Repository](https://github.com/WongKinYiu/yolov7.git)
- [YOLOv7-object-cropping](https://github.com/RizwanMunawar/yolov7-object-cropping.git)
- [easyocr documentation](https://github.com/JaidedAI/EasyOCR.git)
- [kerasocr documentation](https://github.com/faustomorales/keras-ocr.git)
- [pytesseract documentation](https://pypi.org/project/pytesseract/)

### Dataset
You can access raw (not labeled, resized and splitted) dataset [here](https://www.kaggle.com/datasets/mmirzarizkiawan/lowlight-indonesia-lp)
