import api.face_comparer.facenet as facenet


def get_face_comparer(module):
    if module == 'facenet':
        return facenet.FaceComparer()
    else:
        raise ValueError('Module - ' + module + ' not found')
