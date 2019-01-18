import matplotlib.pyplot as plt
import numpy as np
from scipy import misc

import api.services.face_comparer.factory as face_comparer_factory
import api.services.face_detector.factory as face_detector_factory
from api.services.comparer_service import ComparerService


def main(file=None):
    # Load image to compare
    img = misc.imread(file, mode='RGB')

    plt.imshow(np.uint8(img))
    plt.title('Query image')
    plt.savefig('query_image.png')

    # Initialization
    face_detector = face_detector_factory.get_face_detector('default')
    face_detector.initialize()

    face_comparer = face_comparer_factory.get_face_comparer('default')
    face_comparer.initialize(face_comparer.default_model_path, face_detector)

    comparer_service = ComparerService(face_detector, face_comparer, display_result=True)
    comparer_service.compare(0, img)


if __name__ == '__main__':
    main()
