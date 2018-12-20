import os
import cv2
import sys
import queue
import shutil

outpath = "out"
inpath = "bilder"
im_q = queue.Queue()


def init():

    if not os.path.exists(outpath):
        os.makedirs(outpath)
    getImages()
    startClassy()

def getImages():

    for path in os.listdir(inpath):
        if os.path.isfile(os.path.join(inpath, path)):
            im_q.put(path)

    print("Found", im_q.qsize(), "images.")

def startClassy():

    while 1:




        if im_q.qsize() == 0:

            print("Alla bilder klassifierade, bra jobbat!")
            cv2.destroyAllWindows()
            sys.exit()
        image_path = im_q.get()
        print("hej")

        try:
            displayImage(os.path.join(inpath, image_path))
            k = cv2.waitKey(0)

            if k in range(48, 59):
                moveTo((k - 48), image_path)
                cv2.destroyAllWindows()

            elif k == 8:
                undo()

            elif k == 27:
                sys.exit()
                cv2.destroyAllWindows()

        except Exception as e:
            print(e)

def displayImage (path):
    print("Displaying", path)
    im = cv2.imread(path)
    cv2.imshow(path, im)

def moveTo(label, path):
    print("moving", path, "to", label)

    labelpath = os.path.join(outpath, "label" + str(label))

    if not os.path.exists(labelpath):
        os.makedirs(labelpath)
    shutil.copyfile(os.path.join(inpath, path), os.path.join(labelpath, path))



def undo():
    print("undoing")










if __name__ == "__main__":
    init()
