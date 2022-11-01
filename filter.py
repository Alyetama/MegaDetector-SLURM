#!/usr/bin/env python
# coding: utf-8

import shutil
import sys
from glob import glob
from pathlib import Path

from tqdm import tqdm


def main():
    originals_parent_dir = sys.argv[1]

    results_folders = list(Path(originals_parent_dir).rglob('*-results'))
    if '-results' in originals_parent_dir:
        results_folders.extend([Path(originals_parent_dir)])

    for result_folder in results_folders:
        originals_dir = Path(str(result_folder).replace('-results', ''))
        labels_dir = result_folder / 'labels'
        images = [x for x in glob(f'{originals_dir}/*') if Path(x).is_file()]
        labels = sorted(glob(f'{labels_dir}/*'))
        labels_stem = [Path(x).stem for x in labels]
        images_with_detections = sorted(
            [x for x in images if Path(x).stem in labels_stem])

        print(len(images_with_detections), len(labels))
        assert len(images_with_detections) == len(labels)
        for x, y in zip(images_with_detections, labels):
            assert Path(x).stem == Path(y).stem

        with_detections_dir_original = f'{result_folder}/with-detections-original'  # noqa: E501
        Path(with_detections_dir_original).mkdir(exist_ok=True)

        for im in tqdm(images_with_detections):
            shutil.copy2(im, with_detections_dir_original)

        with_detections_dir_bbox = f'{result_folder}/with-detections-bbox'
        without_detections_dir = f'{result_folder}/without-detections'
        Path(with_detections_dir_bbox).mkdir(exist_ok=True)
        Path(without_detections_dir).mkdir(exist_ok=True)

        result_folder_glob = list(result_folder.glob('*.jpg'))
        result_folder_glob.extend(list(result_folder.glob('*.mp4')))

        for im in result_folder_glob:
            if im.stem in labels_stem:
                shutil.move(str(im), with_detections_dir_bbox)
            else:
                shutil.move(str(im), without_detections_dir)


if __name__ == '__main__':
    main()
