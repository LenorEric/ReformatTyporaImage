import sys
import cv2
import numpy as np


def read_chinese(_target_path, _method):
    _image = cv2.imdecode(np.fromfile(_target_path, dtype=np.uint8), _method)
    return _image


if __name__ == '__main__':
    assert len(sys.argv) == 2
    target_path = sys.argv[1]
    tar_img = cv2.imread(target_path, cv2.IMREAD_UNCHANGED)
    diff = 0
    h = 0
    last_letter = 0
    while h < tar_img.shape[0] - diff:
        while tar_img[h + diff][0][3] == 0:
            diff += 3
        if diff != 0:
            tar_img[h] = tar_img[h + diff]
        if tar_img[h].min() <= 250:
            last_letter = h
        h += 1
    tar_img = tar_img[:min(last_letter + 60, h - diff)]
    cv2.imwrite(target_path, tar_img)
    print("Done")
