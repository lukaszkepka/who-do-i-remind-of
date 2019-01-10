
class ComparisonDTO:

    def __init__(self, person_id=0, name='', surname='', image='', similarity_ratio=0.0):
        self.person_id = person_id
        self.name = name
        self.surname = surname
        self.image = image
        self.similarity_ratio = similarity_ratio

    def __repr__(self):
        return "<ComparisonDTO(PersonId=%ld, Name=%s, Surname=%s, Image=%s, SimilarityRatio=%s)>" \
               % (self.person_id, self.name, self.surname, self.image, self.similarity_ratio)