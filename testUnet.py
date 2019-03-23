from model import *
from data import *

print "testing..........."
testGene = testGenerator("/ext/xhzhao/Unet-CT/data/liverCT/test")
# model = unet("unet_membrane.hdf5")
# model = unet("unet_liverCT_fulliamge.hdf5")
model = unet("unet_liverCT_0.hdf5")
# model.load_weights("unet_membrane.hdf5")
results = model.predict_generator(testGene, 10, verbose=1)
# results[results > 0.01] = 1
# results[results <= 0.01] = 0
saveResult("/ext/xhzhao/Unet-CT/data/liverCT_/liver1/pred", results)
