import cv2

import random


def run(s):
    imgshirt=cv2.imread("D://VirTuex//VirTuex//women//"+s)
    face_cascade=cv2.CascadeClassifier(r'D:\VirTuex\VirTuex\haarcascade_frontalface_alt2.xml')
    cap=cv2.VideoCapture(0)
    ret,img = cap.read()
    img_h, img_w = img.shape[:2]

    while True:
        ret,img=cap.read()
        img = cv2.flip(img,1,0)

        musgray = cv2.cvtColor(imgshirt,cv2.COLOR_BGR2GRAY) #grayscale conversion
        ret, orig_mask = cv2.threshold(musgray,150 , 255, cv2.THRESH_BINARY)
        orig_mask_inv = cv2.bitwise_not(orig_mask)
        origshirtHeight, origshirtWidth = imgshirt.shape[:2]
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,
                                            scaleFactor=1.4,
                                            minNeighbors=3,
                                            minSize=(30,30)
                                            )
        for (x,y,w,h) in faces:
                #cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

                face_w = w
                face_h = h
                face_x1 = x
                face_x2 = face_x1 + face_h
                face_y1 = y
                face_y2 = face_y1 + face_h

                # set the shirt size in relation to tracked face
                shirtWidth = 3 * face_w
                shirtHeight = int(shirtWidth * origshirtHeight / origshirtWidth)


                shirt_x1 = face_x2 - int(face_w) - int(shirtWidth/2) - 5  #setting shirt centered wrt recognized face
                shirt_x2 = shirt_x1 + shirtWidth +  int(face_w) +5
                shirt_y1 = face_y2  # some padding between face and upper shirt. Depends on the shirt img
                shirt_y2 = shirt_y1 + shirtHeight + int(2.5*h)

                # Check for clipping
                if shirt_x1 < 0:
                    shirt_x1 = 0
                if shirt_y1 < 0:
                    shirt_y1 = 0
                if shirt_x2 > img_w:
                    shirt_x2 = img_w
                if shirt_y2 > img_h:
                    shirt_y2 = img_h

                shirtWidth = shirt_x2 - shirt_x1
                shirtHeight = shirt_y2 - shirt_y1
                if shirtWidth < 0 or shirtHeight < 0:
                    continue

                # Re-size the original image and the masks to the shirt sizes
                shirt = cv2.resize(imgshirt, (shirtWidth,shirtHeight), interpolation = cv2.INTER_AREA)
                #resize all,the masks you made,the originla image,everything
                mask = cv2.resize(orig_mask, (shirtWidth,shirtHeight), interpolation = cv2.INTER_AREA)
                mask_inv = cv2.resize(orig_mask_inv, (shirtWidth,shirtHeight), interpolation = cv2.INTER_AREA)

                # take ROI for shirt from background equal to size of shirt image
                roi = img[shirt_y1:shirt_y2, shirt_x1:shirt_x2]


                # roi_bg contains the original image only where the shirt is not
                # in the region that is the size of the shirt.
                roi_bg = cv2.bitwise_and(roi,roi,mask = mask)
                roi_fg = cv2.bitwise_and(shirt,shirt,mask = mask_inv)
                dst = cv2.add(roi_bg,roi_fg)
                img[shirt_y1:shirt_y2, shirt_x1:shirt_x2] = dst

                break


        font = cv2.FONT_HERSHEY_PLAIN  # Creates a font
        x = 10  # position of text
        
        cv2.putText(img, "press 'c' key for snapshot", (x, 440), font, .8, (0, 100, 0),1)
        cv2.putText(img, "press 'q' key to come back agaiin", (x,460), font, .8, (0, 100, 0),1)
        cv2.namedWindow("Virtual Dressing Room", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Virtual Dressing Room", int(img.shape[1] * 1.4), int(img.shape[0] * 1.9))
        cv2.imshow('Virtual Dressing Room', img)
        key = cv2.waitKey(10)
                
        if key & 0xFF == ord('c'):  # save on pressing 'c'
            j=50
            while j>=10:
                ret,img=cap.read()
                img = cv2.flip(img,1,0)
                imgshirt=cv2.imread("D://VirTuex//VirTuex//women//"+s)
                face_cascade=cv2.CascadeClassifier(r'D:\VirTuex\VirTuex\haarcascade_frontalface_alt2.xml')
                musgray = cv2.cvtColor(imgshirt,cv2.COLOR_BGR2GRAY) #grayscale conversion
                ret, orig_mask = cv2.threshold(musgray,150 , 255, cv2.THRESH_BINARY)
                orig_mask_inv = cv2.bitwise_not(orig_mask)
                origshirtHeight, origshirtWidth = imgshirt.shape[:2]
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces=face_cascade.detectMultiScale(gray,
                                                    scaleFactor=1.4,
                                                    minNeighbors=3,
                                                    minSize=(30,30)
                                                    )
                for (x,y,w,h) in faces:
                        #cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

                        face_w = w
                        face_h = h
                        face_x1 = x
                        face_x2 = face_x1 + face_h
                        face_y1 = y
                        face_y2 = face_y1 + face_h

                        # set the shirt size in relation to tracked face
                        shirtWidth = 3 * face_w
                        shirtHeight = int(shirtWidth * origshirtHeight / origshirtWidth)

                        shirt_x1 = face_x2 - int(face_w) - int(shirtWidth/2) - 5  #setting shirt centered wrt recognized face
                        shirt_x2 = shirt_x1 + shirtWidth +  int(face_w) +5
                        shirt_y1 = face_y2  # some padding between face and upper shirt. Depends on the shirt img
                        shirt_y2 = shirt_y1 + shirtHeight + int(2.5*h)

                        # Check for clipping
                        if shirt_x1 < 0:
                            shirt_x1 = 0
                        if shirt_y1 < 0:
                            shirt_y1 = 0
                        if shirt_x2 > img_w:
                            shirt_x2 = img_w
                        if shirt_y2 > img_h:
                            shirt_y2 = img_h

                        shirtWidth = shirt_x2 - shirt_x1
                        shirtHeight = shirt_y2 - shirt_y1
                        if shirtWidth < 0 or shirtHeight < 0:
                            continue

                        # Re-size the original image and the masks to the shirt sizes
                        shirt = cv2.resize(imgshirt, (shirtWidth,shirtHeight), interpolation = cv2.INTER_AREA)
                        #resize all,the masks you made,the originla image,everything
                        mask = cv2.resize(orig_mask, (shirtWidth,shirtHeight), interpolation = cv2.INTER_AREA)
                        mask_inv = cv2.resize(orig_mask_inv, (shirtWidth,shirtHeight), interpolation = cv2.INTER_AREA)

                        # take ROI for shirt from background equal to size of shirt image
                        roi = img[shirt_y1:shirt_y2, shirt_x1:shirt_x2]


                        # roi_bg contains the original image only where the shirt is not
                        # in the region that is the size of the shirt.
                        roi_bg = cv2.bitwise_and(roi,roi,mask = mask)
                        roi_fg = cv2.bitwise_and(shirt,shirt,mask = mask_inv)
                        dst = cv2.add(roi_bg,roi_fg)
                        img[shirt_y1:shirt_y2, shirt_x1:shirt_x2] = dst

                        break
                if j%10 == 0:
                    # specify the font and draw the countdown using puttext
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(img,str(j//10),(250,250), font, 7,(255,255,255),10,cv2.LINE_AA)
                cv2.imshow('Virtual Dressing Room',img)
                cv2.waitKey(5)
                j = j-1
            else:
                ret,img=cap.read()
                img = cv2.flip(img,1,0)
                imgshirt=cv2.imread("D://VirTuex//VirTuex//women//"+s)

                musgray = cv2.cvtColor(imgshirt,cv2.COLOR_BGR2GRAY) #grayscale conversion
                ret, orig_mask = cv2.threshold(musgray,150 , 255, cv2.THRESH_BINARY)
                orig_mask_inv = cv2.bitwise_not(orig_mask)
                origshirtHeight, origshirtWidth = imgshirt.shape[:2]
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces=face_cascade.detectMultiScale(gray,
                                                    scaleFactor=1.4,
                                                    minNeighbors=3,
                                                    minSize=(30,30)
                                                    )
                for (x,y,w,h) in faces:
                    #cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

                    face_w = w
                    face_h = h
                    face_x1 = x
                    face_x2 = face_x1 + face_h
                    face_y1 = y
                    face_y2 = face_y1 + face_h

                    # set the shirt size in relation to tracked face
                    shirtWidth = 3 * face_w
                    shirtHeight = int(shirtWidth * origshirtHeight / origshirtWidth)


                    shirt_x1 = face_x2 - int(face_w) - int(shirtWidth/2) - 5  #setting shirt centered wrt recognized face
                    shirt_x2 = shirt_x1 + shirtWidth +  int(face_w) +5
                    shirt_y1 = face_y2  # some padding between face and upper shirt. Depends on the shirt img
                    shirt_y2 = shirt_y1 + shirtHeight + int(2.5*h)
                    # Check for clipping
                    if shirt_x1 < 0:
                        shirt_x1 = 0
                    if shirt_y1 < 0:
                        shirt_y1 = 0
                    if shirt_x2 > img_w:
                        shirt_x2 = img_w
                    if shirt_y2 > img_h:
                        shirt_y2 = img_h

                    shirtWidth = shirt_x2 - shirt_x1
                    shirtHeight = shirt_y2 - shirt_y1
                    if shirtWidth < 0 or shirtHeight < 0:
                        continue

                    # Re-size the original image and the masks to the shirt sizes
                    shirt = cv2.resize(imgshirt, (shirtWidth,shirtHeight), interpolation = cv2.INTER_AREA)
                    #resize all,the masks you made,the originla image,everything
                    mask = cv2.resize(orig_mask, (shirtWidth,shirtHeight), interpolation = cv2.INTER_AREA)
                    mask_inv = cv2.resize(orig_mask_inv, (shirtWidth,shirtHeight), interpolation = cv2.INTER_AREA)

                    # take ROI for shirt from background equal to size of shirt image
                    roi = img[shirt_y1:shirt_y2, shirt_x1:shirt_x2]


                    # roi_bg contains the original image only where the shirt is not
                    # in the region that is the size of the shirt.
                    roi_bg = cv2.bitwise_and(roi,roi,mask = mask)
                    roi_fg = cv2.bitwise_and(shirt,shirt,mask = mask_inv)
                    dst = cv2.add(roi_bg,roi_fg)
                    img[shirt_y1:shirt_y2, shirt_x1:shirt_x2] = dst

                    break
                # Display the clicked frame for 1 sec.
                # You can increase time in waitKey also

                cv2.imshow('Virtual Dressing Room',img)

                # Save the frame
                rand = random.randint(1, 999999)
                cv2.imwrite('D:\\VirTuex\\VirTuex\\Captues\\'+str(rand)+'.png', img)
                cv2.putText(img,"Processing...",(100,250),font, 1,(255,0,100),1,cv2.LINE_AA)
                cv2.waitKey(50)

                cv2.imshow('Virtual Dressing Room',img)

        if key & 0xFF  == ord('q'):
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,"See You Later",(20,250), font, 2.5,(255,0,0),10,cv2.LINE_AA)
            cv2.imshow('Virtual Dressing Room', img)
            cv2.waitKey(1000)
            break
            sys.exit()
    cap.release() # Destroys the cap object
    cv2.destroyAllWindows() # Destroys all the windows created by imshow


