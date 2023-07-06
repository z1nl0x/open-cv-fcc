import cv2 as cv

# Video, Images and Live Video
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# img = cv.imread('Photos/cat.jpg')
# resized_image = rescaleFrame(img)
# cv.imshow('Car', img)
# cv.imshow('Image', resized_image)

# Only Live Video
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

# Reading Videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)