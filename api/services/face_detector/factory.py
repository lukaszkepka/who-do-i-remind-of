import api.services.face_detector.PRO.detect_face as PRO


def get_face_detector(module):
    if module == 'PRO' or module == 'default':
        return PRO.FaceDetector()
    else:
        raise ValueError('Module - ' + module + ' not found')
