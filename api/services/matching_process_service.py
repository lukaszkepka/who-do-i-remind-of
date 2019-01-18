from api.services.face_comparer.compare import main


class MatchingProcessService:

    def run_matching_process(self, image_file, dataset_id=1):
        main(image_file)
