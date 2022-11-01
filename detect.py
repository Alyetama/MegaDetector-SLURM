#!/usr/bin/env python
# coding: utf-8

import sys
from pathlib import Path

from loguru import logger
from yolov5.detect import parse_opt, main as detect_main


def main():
    src_dir = Path(sys.argv[1])
    sys.argv = sys.argv[:1]

    for x in src_dir.rglob('*.*'):
        x.rename(x.with_suffix(x.suffix.lower()))

    dirs = [x for x in src_dir.rglob('*') if Path(x).is_dir()]
    dirs.extend([src_dir])

    dirs_with_images = [
        x for x in dirs if any(x for x in Path(x).glob('*.jpg'))
    ]

    logger.debug(f'Dirs w/ images: {dirs_with_images}')

    for cur_dir in dirs_with_images:
        logger.debug(f'Current dir: {cur_dir}')
        results_dir_name = Path(f'{cur_dir}-results')
        logger.debug(f'Results dir name: {results_dir_name}')

        if results_dir_name.exists() or any(
                x for x in ['-results', '-detections'] if x in cur_dir.name):
            logger.warning('Results dir already exists! Skipping...')
            continue

        opts = vars(parse_opt())
        custom_opts = {
            'exist_ok': True,
            'weights': 'md_v5a.0.0.pt',
            'source': cur_dir,
            'device': 'cpu',
            'save_txt': True,
            'save_conf': True,
            'project': results_dir_name,
            'name': ''
        }
        opts.update(custom_opts)

        detect_main(**opts)


if __name__ == '__main__':
    main()
