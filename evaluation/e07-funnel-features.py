import time
import numpy as np
from common.metaguard import metaguard
from common.dmm import dmm

# Start measuring performance
start_time = time.time()

# Load the input data
print("Loading input data...")
replays = np.load('../data/user-identification/user-replays.npy')

# Control group
print("Processing control feautres...")
np.save('./anonymity/funnel-control', replays)

# MetaGuard group
print("Processing MetaGuard feautres...")
anonymized = metaguard(replays.reshape(-1, 900, 21))
np.save('./anonymity/funnel-metaguard', np.array(anonymized).reshape(-1, 20, 900, 21))

# Deep motion masking group
print("Processing deep motion masking feautres...")
noise = np.random.normal(size=(2000,32)).astype('float16')
noise = np.repeat(noise, 10, axis=0)
anonymized = dmm(replays.reshape(-1, 900, 21), noise)
np.save('./anonymity/funnel-dmm', np.array(anonymized).reshape(-1, 20, 900, 21))

# Log performance results
end_time = time.time()
print("Finished in %s Minutes" % ((end_time - start_time) / 60))
