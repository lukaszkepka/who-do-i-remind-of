
class ComparisonDTO:

    def __init__(self, person_id=0, name='', image='', similarity_ratio=0.0, shape=None):
        self.person_id = person_id
        self.name = name
        self.image = image
        self.similarity_ratio = similarity_ratio
        self.image_shape = shape

    def __repr__(self):
        return "<ComparisonDTO(PersonId=%ld, Name=%s, Image=%s, SimilarityRatio=%s)>" \
               % (self.person_id, self.name, self.image, self.similarity_ratio)
