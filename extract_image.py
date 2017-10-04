import csv
import cv2


CSV_FILE = 'dayTraining/dayClip1/frameAnnotationsBULB.csv'
with open(CSV_FILE, 'rb') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')

    num_img_saved = 0
    for index, row in enumerate(reader):

        file_name = row['Filename']
        # convert 'dayTraining/dayClip1--00000.png' to 'dayTraining/dayClip1/frames/dayClip1--00000.png'
        file_name = file_name.replace('dayTraining/', 'dayTraining/dayClip1/frames/')

        img = cv2.imread(file_name, cv2.IMREAD_COLOR)
        upper_left = (int(row['Upper left corner X']), int(row['Upper left corner Y']))
        lower_right = (int(row['Lower right corner X']), int(row['Lower right corner Y']))

        MIN_BULB_WIDTH = 10
        if (lower_right[0] - upper_left[0] > MIN_BULB_WIDTH or
                lower_right[1] - upper_left[1] > MIN_BULB_WIDTH):
            center_x = int((lower_right[0] + upper_left[0]) / 2)
            center_y = int((lower_right[1] + upper_left[1]) / 2)
            width = 200
            margin = width/2

            upper_left = (center_x - margin, center_y - margin)
            lower_right = (upper_left[0] + width, upper_left[1] + width)
            flag = row['Annotation tag']

            # crop and save image
            crop_img = img[upper_left[1]:lower_right[1], upper_left[0]:lower_right[0]].copy()
            cropped_file_name = 'data/{}-cropped-{}.png'.format(flag, index)
            # print('write cropped image:', cropped_file_name)
            if crop_img.shape != (width, width, 3):
                print('image was corpped incorrectly, skip')
                continue

            cv2.imwrite(cropped_file_name, crop_img)

            # # draw bounding box and save image
            # color = (255, 255, 0)
            # thickness = 2
            # cv2.rectangle(img, upper_left, lower_right, color, thickness)
            # # print('write bounging box image:', cropped_file_name)
            # bb_file_name = 'data/{}-bb-{}.png'.format(flag, index)
            # cv2.imwrite(bb_file_name, img)

            num_img_saved += 1
        if num_img_saved > 50:
            # # print all keys in row
            # for key in row:
            #     print key
            break
