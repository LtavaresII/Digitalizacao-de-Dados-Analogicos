import cv2
from pyzbar import pyzbar
import numpy as np

#cap = cv2.VideoCapture(1)

def get_frame(cap):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    _, frame = cap.read()

    if frame is None:
        raise FileNotFoundError("Não foi possível carregar a imagem.")

    return frame

def read_qr_codes(frame):
    
    qr_codes = pyzbar.decode(frame)
    positions = {}
    
    for qr_code in qr_codes:
        data = qr_code.data.decode('utf-8')
        x, y, w, h = qr_code.rect
        positions[data] = (x + w // 2, y + h // 2)
        
    return positions

def centralize_image(frame, positions):
    required_positions = ['top_left', 'bottom_left', 'top_right', 'bottom_right']
    
    if all(pos in positions for pos in required_positions):
        
        top_left = positions['top_left']
        bottom_left = positions['bottom_left']
        top_right = positions['top_right']
        bottom_right = positions['bottom_right']
        
        src = [top_left,bottom_left,top_right,bottom_right]
        src = np.float32(src)
        
        height, width, _ = frame.shape
        dst = [[0,0],[0,height],[width,0],[width,height]]
        dst = np.float32(dst)
        
        M = cv2.getPerspectiveTransform(src,dst)
        frame_centered = cv2.warpPerspective(frame, M, (width, height))

        return frame_centered
    else:
        return frame

def get_brightness(frame_centered):
    # First column
    red_1 = frame_centered[149:177, 55:83]
    green_1 = frame_centered[244:272, 58:86]
    blue_1 = frame_centered[336:364, 63:91]
    # Second column
    red_2 = frame_centered[149:177, 160:188]
    green_2 = frame_centered[243:271, 161:189]
    blue_2 = frame_centered[336:364, 164:192]
    # Third column
    red_3 = frame_centered[149:177, 266:294]
    green_3 = frame_centered[243:271, 268:296]
    blue_3 = frame_centered[336:364, 271:299]
    # Fourth column
    red_4 = frame_centered[136:190, 374:402]
    green_4 = frame_centered[246:274, 374:402]
    blue_4 = frame_centered[336:364, 374:402]
    # Fifth column
    red_5 = frame_centered[150:178, 478:506]
    green_5 = frame_centered[245:273, 478:506]
    blue_5 = frame_centered[332:360, 478:506]
    # Sixth column
    red_6 = frame_centered[149:177, 583:611]
    green_6 = frame_centered[241:269, 581:609] 
    blue_6 = frame_centered[333:361, 582:610]
    # Seventh column
    red_7 = frame_centered[150:178, 687:715]
    green_7 = frame_centered[242:270, 686:714] 
    blue_7 = frame_centered[333:361, 684:712]
    # Eighth column
    red_8 = frame_centered[150:178, 795:823]
    green_8 = frame_centered[242:270, 791:819] 
    blue_8 = frame_centered[333:361, 793:821]
    # Ninth column
    red_9 = frame_centered[150:178, 902:930]
    green_9 = frame_centered[242:270, 897:925] 
    blue_9 = frame_centered[337:365, 895:923]
    # Tenth column
    red_10 = frame_centered[150:178, 1007:1035]
    green_10 = frame_centered[243:271, 1001:1029] 
    blue_10 = frame_centered[336:364, 997:1025]
    # Eleventh column
    red_11 = frame_centered[150:178, 1111:1139]
    green_11 = frame_centered[245:273, 1105:1133] 
    white_1 = frame_centered[335:363, 1099:1127]
    # Twelfth column
    red_12 = frame_centered[156:184, 1214:1242]
    green_12 = frame_centered[246:272, 1206:1234] 
    white_2 = frame_centered[335:363, 1199:1227]
    # Thirteenth column
    red_13 = frame_centered[500:528, 78:106]
    green_13 = frame_centered[588:616, 82:110] 
    # Fourteenth column
    red_14 = frame_centered[500:528, 178:206]
    green_14 = frame_centered[588:616, 181:209] 
    # Fifteenth column
    red_15 = frame_centered[503:531, 280:308]
    green_15 = frame_centered[589:617, 281:309] 
    # Sixteenth column
    red_16 = frame_centered[503:531, 483:511]
    green_16 = frame_centered[588:616, 483:511] 

    # Get the Brightness

    ROI = [red_1,green_1,blue_1,red_2,green_2,blue_2,red_3,green_3,blue_3,red_4,green_4,blue_4,red_5,green_5,blue_5,red_6,green_6,blue_6,red_7,green_7,blue_7,red_8,green_8,blue_8,red_9,green_9,blue_9,red_10,green_10,blue_10]
    ROI2 = [red_11,green_11,white_1,red_12,green_12,white_2]
    ROI3 = [red_13,green_13,red_14,green_14,red_15,green_15,red_16,green_16]

    ROIxy = [[69,163],[72,258],[77,350],[174,163],[175,257],[178,350],[280,163],[282,257],[285,350],[388,163],[388,260],[388,350],[492,164],[492,259],[492,346],[597,163],[595,255],[596,347],[701,164],[700,256],[698,347],[809,164],[805,256],[807,347],[916,164],[911,256],[909,351],[1021,164],[1015,257],[1011,350]]
    ROIxy2 = [[1125,164],[1119,259],[1113,349],[1228,170],[1220,260],[1213,349]]
    ROIxy3 = [[92,514],[96,602],[192,514],[195,602],[294,517],[295,603],[497,517],[497,602]]
    
    brigth1 = []
    brigth2 = []
    brigth3 = []

    # Intensity
    # Red >= 78
    # Green >= 126
    # Blue >= 73
    # White >= 204

    for i in ROI:
        img = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
        avg = np.mean(img)
        brigth1.append(avg)

    for i in ROI2:
        img = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
        avg = np.mean(img)
        brigth2.append(avg)

    for i in ROI3:
        img = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
        avg = np.mean(img)
        brigth3.append(avg)

    color_red_on = (0,0,255)
    color_red_off = (0,0,127)
    color_green_on = (0,255,0)
    color_green_off = (0,127,0)
    color_blue_on = (255,0,0)
    color_blue_off = (127,0,0)
    color_white_on = (255,255,255)
    color_white_off = (127,127,127)
    thickness = 2
    radius = 14

    on_off = []
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    for i in range(0,29,3):
        if brigth1[i] >= 78:
            on_off.append(0)
            cv2.circle(frame_centered, (ROIxy[i][0],ROIxy[i][1]), radius, color_red_on, thickness)
            cv2.putText(frame_centered,"Red On",(ROIxy[i][0]-radius,ROIxy[i][1]-radius),font,0.5,(0,0,0),thickness)
        else:
            on_off.append(4)
            cv2.circle(frame_centered, (ROIxy[i][0],ROIxy[i][1]), radius, color_red_off, thickness)
            cv2.putText(frame_centered,"Red Off",(ROIxy[i][0]-radius,ROIxy[i][1]-radius),font,0.5,(0,0,0),thickness)
        if brigth1[i+1] >= 126:
            on_off.append(1)
            cv2.circle(frame_centered, (ROIxy[i+1][0],ROIxy[i+1][1]), radius, color_green_on, thickness)
            cv2.putText(frame_centered,"Green On",(ROIxy[i+1][0]-radius,ROIxy[i+1][1]-radius),font,0.5,(0,0,0),thickness)
        else:
            on_off.append(5)
            cv2.circle(frame_centered, (ROIxy[i+1][0],ROIxy[i+1][1]), radius, color_green_off, thickness)
            cv2.putText(frame_centered,"Green Off",(ROIxy[i+1][0]-radius,ROIxy[i+1][1]-radius),font,0.5,(0,0,0),thickness)
        if brigth1[i+2] >= 73:
            on_off.append(2)
            cv2.circle(frame_centered, (ROIxy[i+2][0],ROIxy[i+2][1]), radius, color_blue_on, thickness)
            cv2.putText(frame_centered,"Blue On",(ROIxy[i+2][0]-radius,ROIxy[i+2][1]-radius),font,0.5,(0,0,0),thickness)
        else:
            on_off.append(6)
            cv2.circle(frame_centered, (ROIxy[i+2][0],ROIxy[i+2][1]), radius, color_blue_off, thickness)
            cv2.putText(frame_centered,"Blue Off",(ROIxy[i+2][0]-radius,ROIxy[i+2][1]-radius),font,0.5,(0,0,0),thickness)

    for i in range(0,5,3):
        if brigth2[i] >= 78:
            on_off.append(0)
            cv2.circle(frame_centered, (ROIxy2[i][0],ROIxy2[i][1]), radius, color_red_on, thickness)
            cv2.putText(frame_centered,"Red On",(ROIxy2[i][0]-radius,ROIxy2[i][1]-radius),font,0.5,(0,0,0),thickness)
        else:
            on_off.append(4)
            cv2.circle(frame_centered, (ROIxy2[i][0],ROIxy2[i][1]), radius, color_red_off, thickness)
            cv2.putText(frame_centered,"Red Off",(ROIxy2[i][0]-radius,ROIxy2[i][1]-radius),font,0.5,(0,0,0),thickness)
        if brigth2[i+1] >= 126:
            on_off.append(1)
            cv2.circle(frame_centered, (ROIxy2[i+1][0],ROIxy2[i+1][1]), radius, color_green_on, thickness)
            cv2.putText(frame_centered,"Green On",(ROIxy2[i+1][0]-radius,ROIxy2[i+1][1]-radius),font,0.5,(0,0,0),thickness)
        else:
            on_off.append(5)
            cv2.circle(frame_centered, (ROIxy2[i+1][0],ROIxy2[i+1][1]), radius, color_green_off, thickness)
            cv2.putText(frame_centered,"Green Off",(ROIxy2[i+1][0]-radius,ROIxy2[i+1][1]-radius),font,0.5,(0,0,0),thickness)
        if brigth2[i+2] >= 185:
            on_off.append(3)
            cv2.circle(frame_centered, (ROIxy2[i+2][0],ROIxy2[i+2][1]), radius, color_white_on, thickness)
            cv2.putText(frame_centered,"White On",(ROIxy2[i+2][0]-radius,ROIxy2[i+2][1]-radius),font,0.5,(0,0,0),thickness)
        else:
            on_off.append(7)
            cv2.circle(frame_centered, (ROIxy2[i+2][0],ROIxy2[i+2][1]), radius, color_white_off, thickness)
            cv2.putText(frame_centered,"White Off",(ROIxy2[i+2][0]-radius,ROIxy2[i+2][1]-radius),font,0.5,(0,0,0),thickness)

    for i in range(0,7,2):
        if brigth3[i] >= 78:
            on_off.append(0)
            cv2.circle(frame_centered, (ROIxy3[i][0],ROIxy3[i][1]), radius, color_red_on, thickness)
            cv2.putText(frame_centered,"Red On",(ROIxy3[i][0]-radius,ROIxy3[i][1]-radius),font,0.5,(0,0,0),thickness)
        else:
            on_off.append(4)
            cv2.circle(frame_centered, (ROIxy3[i][0],ROIxy3[i][1]), radius, color_red_off, thickness)
            cv2.putText(frame_centered,"Red Off",(ROIxy3[i][0]-radius,ROIxy3[i][1]-radius),font,0.5,(0,0,0),thickness)
        if brigth3[i+1] >= 126:
            on_off.append(1)
            cv2.circle(frame_centered, (ROIxy3[i+1][0],ROIxy3[i+1][1]), radius, color_green_on, thickness)
            cv2.putText(frame_centered,"Green On",(ROIxy3[i+1][0]-radius,ROIxy3[i+1][1]-radius),font,0.5,(0,0,0),thickness)
        else:
            on_off.append(5)
            cv2.circle(frame_centered, (ROIxy3[i+1][0],ROIxy3[i+1][1]), radius, color_green_off, thickness)
            cv2.putText(frame_centered,"Green Off",(ROIxy3[i+1][0]-radius,ROIxy3[i+1][1]-radius),font,0.5,(0,0,0),thickness)

    return frame_centered, on_off

#while(True):
    
    #_, frame = cap.read()
    
    #frame = cv2.imread('PainelQR.jpg')
    #frame = cv2.resize(frame, (1280, 720))

    #if frame is None:
    #    print("Cannot open the video cam")
    #    break
    
    #positions = read_qr_codes(frame)
    
    #frame_centered = centralize_image(frame, positions)

    #frame_bright, on_off = get_brightness(frame_centered)

    #cv2.imshow('QR_Reader', frame_bright)
    
    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #break
    
#cap.release()
#cv2.destroyAllWindows() 
# https://medium.com/@anandkushagra2898/image-brightness-calculator-9202128d7f42