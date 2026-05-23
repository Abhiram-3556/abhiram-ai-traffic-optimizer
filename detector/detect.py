from ultralytics import YOLO
import cv2

MODEL=None

VEHICLES={'car','bus','truck','motorcycle'}

def load_model():
    global MODEL
    if MODEL is None:
        MODEL=YOLO('yolov8n.pt')
    return MODEL

def detect(frame):
    model=load_model()
    results=model(frame,verbose=False)
    count=0
    annotated=frame.copy()

    for r in results:
        for box in r.boxes:
            cls=int(box.cls[0])
            name=model.names[cls]
            if name in VEHICLES:
                count+=1
                x1,y1,x2,y2=map(int,box.xyxy[0])
                cv2.rectangle(annotated,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.putText(annotated,name,(x1,y1-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)

    return annotated,count
