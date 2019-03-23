from model import *
from data import *

data_gen_args = dict(rotation_range=0.2,
                    width_shift_range=0.05,
                    height_shift_range=0.05,
                    shear_range=0.05,
                    zoom_range=0.05,
                    horizontal_flip=True,
                    fill_mode='nearest')
myGene = trainGenerator(2,'data/liverCT/train','image','label',data_gen_args,save_to_dir = None)
model = unet()

model_checkpoint = ModelCheckpoint('unet_liverCT_fulliamge.hdf5', monitor='loss',verbose=1, save_best_only=True)
print "training............"
model.fit_generator(myGene, steps_per_epoch=3000, epochs=50, callbacks=[model_checkpoint])

