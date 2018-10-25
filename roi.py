import sys
import cv2
import pytesseract
import vertical
import rectangle
import Cell_test
import tm
def row_height(lines):
    avg_distance = 0
    count=0
    if lines is None:
        return 0
    else:
        for idx,line in enumerate(lines):
            if idx == len(lines)-1:
                break

            avg_distance +=  max(lines[idx+1][0][1],lines[idx+1][0][3]) - min(line[0][1],line[0][3])
            count += 1

        avg_distance /= count
        return int(avg_distance)


def create_row(img,horizontal_lines,vertical_lines):
    row_size = row_height(horizontal_lines)
    print("Row Height : " ,row_size)
    row,col = img.shape[:-1]
    counter = 0
    for index,line in enumerate(horizontal_lines) :
        if index == len(horizontal_lines)-1:
            # roi = img[line[0][1]:row,:,:]
            break
        else:
            roi = img[min(line[0][1],line[0][3]):max(horizontal_lines[index+1][0][1],horizontal_lines[index+1][0][3]),:,:]

        roi_row,roi_col,_ = roi.shape
        #print(roi_row)
        if roi_row > 10:
        # if roi_row > row_size :
            # roi = rectangle.thresh(roi)
            # print(pytesseract.image_to_string(roi))
        	# vertical.detect(roi)
            # cv2.imshow("ROI",roi)
            # cv2.waitKey(0)

            print()
            counter += 1
            if counter > 3:
                print()
                for idx,ver_line in enumerate(vertical_lines):
                    if idx == len(vertical_lines)-1:
                        break
                    cells = roi[:,ver_line:vertical_lines[idx+1]]
                    # cv2.imshow('cells',cells)
                    # if cv2.waitKey(0) == ord('n'):
                    #     tm.predict(cells)
                    # cv2.waitKey(0)
                    # cv2.destroyAllWindows()
                    cv2.imwrite("temp_img.jpg",cells)
                    # cv2.imshow("Cells",cells)
                    # cv2.waitKey(0)
                    haha = Cell_test.printed_text("temp_img.jpg")
                    print (haha,end=' ')
                    # if cv2.waitKey(0) == ord('q'):
                        # sys.exit(0)
