import numpy as np
import skimage.io as io
import os


def dice_score(path1, path2, num_image):
    area_A = 0
    area_B = 0
    area_C = 0
    sum = 0
    for i in range(num_image):
        img1 = io.imread(os.path.join(path1,"%d.jpg"%i),as_grey = True)
        img2 = io.imread(os.path.join(path2,"%d.jpg"%i),as_grey = True)
        img2=img2.astype("float64")
        for a in range(512):
            for b in range(512):
                if img1[a, b] > 0.0:
                    area_A = area_A + 1
        print area_A

        for a in range(512):
            for b in range(512):
                if img2[a, b] > 0.0:
                    area_B = area_B + 1
        print area_B

        for a in range(512):
            for b in range(512):
                if img1[a, b] > 0.0 and img2[a, b] > 0.0:
                    area_C = area_C + 1
        print area_C

        # if area_A == 0.0 and area_B == 0.0:
        #     dice = 1

        dice = (2.0 * area_C)/(area_A + area_B + 0.0)
        sum = sum + dice
        print 'Dice_score{}: {}'.format(i, dice)

    avg = sum / num_image
    print 'Dice_avg: {}'.format(avg)
    print '--------------------------------------------------------'


def voe_err(path1, path2, num_image):
    area_C = 0
    area_D = 0
    sum1 = 0
    for i in range(num_image):
        img1 = io.imread(os.path.join(path1,"%d.jpg"%i),as_grey = True)
        img2 = io.imread(os.path.join(path2,"%d.jpg"%i),as_grey = True)
        img2 = np.float64(img2)
        for a in range(512):
            for b in range(512):
                if img1[a, b] > 0.0 and img2[a, b] > 0.0:
                    area_C = area_C + 1
        # print area_C

        for a in range(512):
            for b in range(512):
                if img1[a, b] > 0.0 or img2[a, b] > 0.0:
                    area_D = area_D + 1
        # print area_D
        voe = 1.0 - area_C / (area_D + 0.0)
        sum1 = sum1 + voe

        print 'Voe_err{}: {}'.format(i, 1.0 - area_C / (area_D + 0.0))
    print 'sum:{}'.format(sum1)
    avg = sum1 / num_image
    print 'Voe_avg: {}'.format(avg)
    print '--------------------------------------------------------'


def rvd_err(path1, path2, num_image):
    area_A = 0
    area_B = 0
    sum = 0
    for i in range(num_image):
        img1 = io.imread(os.path.join(path1, "%d.jpg" % i), as_grey=True)
        img2 = io.imread(os.path.join(path2, "%d.jpg" % i), as_grey=True)
        img2 = np.float64(img2)
        for a in range(512):
            for b in range(512):
                if img1[a, b] > 0.0:
                    area_A = area_A + 1
        # print area_A

        for a in range(512):
            for b in range(512):
                if img2[a, b] > 0.0:
                    area_B = area_B + 1
        # print area_B
        rvd = (area_B - area_A + 0.0) / (area_A + 0.0)
        sum = sum + rvd

        print 'Rvd_err{}: {}'.format(i, (area_B - area_A + 0.0) / (area_A + 0.0))
    avg = sum / num_image
    print 'Rvd_avg: {}'.format(avg)
    print '--------------------------------------------------------'


if __name__ == '__main__':
    path1 = '/ext/xhzhao/Unet-CT/evaluation/full_tumor_prediction'
    path2 = '/ext/xhzhao/Unet-CT/evaluation/full_tumor_label'
    num_image = 30
   # dice_score(path1, path2, num_image)

    voe_err(path1, path2, num_image)

   # rvd_err(path1, path2, num_image)
