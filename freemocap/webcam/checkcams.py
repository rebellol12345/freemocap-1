from tqdm import tqdm
import cv2

def TestDevice(source):
   cap = cv2.VideoCapture(source,cv2.CAP_DSHOW) 
   #if cap is None or not cap.isOpened():
       #print('Warning: unable to open video source: ', source)
   
   if cap.isOpened():
        #print('Opened: ',source)
        #print('Exposure: '+ str(cap.get(cv2.CAP_PROP_EXPOSURE)))
        #time.sleep(3)
        cap.release()
        cv2.destroyAllWindows() 
        open_cam = source
        return open_cam
   else:
        return None 

def CreateAvailableCamList():
    openCamList = []
    for x in tqdm(range(20)):#range 20 right now to be safe
       openCamera = TestDevice(x)
       if openCamera is not None:
          openCamList.append(openCamera)
    
    return openCamList