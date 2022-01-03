import numpy as np

def amplitude_encode(img_data):
    rms = np.sqrt(np.sum(np.sum(img_data**2, axis=1)))

    norm_image = []
    for arr in img_data:
        for ele in arr:
            norm_image.append(ele / rms)

    return np.array(norm_image)