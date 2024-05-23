import fiftyone as fo


class Preprocessor:
    """
    Preprocessor process the images to create a dataset that is ready for the downstream machine learning pipeline
    """
    def __init__(self, image_folder_path, coco_file_paths):
        self.image_folder_path = image_folder_path
        assert type(coco_file_paths) is list
        self.coco_file_paths = coco_file_paths
        self.dataset = None

    def create_dataset(self):
        coco_dataset = fo.Dataset.from_dir(
            dataset_type=fo.types.COCODetectionDataset,
            data_path=self.image_folder_path,
            labels_path=self.coco_file_paths[0],
        )
        for coco_path in self.coco_file_paths[1:]:
            coco_dataset.merge_dir(
                dataset_type=fo.types.COCODetectionDataset,
                data_path=self.image_folder_path,
                labels_path=coco_path,
            )
        self.dataset = coco_dataset
        return self.dataset
