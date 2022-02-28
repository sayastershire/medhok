#!/usr/bin/env python3
from sys import argv
import logging

from loader.audio import Audio
import config as c

# STARTUP PARAMETERS
SERIALIZE_NORMALIZE = False

if __name__ == '__main__':
    # Debug
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)

    if len(argv) > 1:
        if argv[1] == 'extract':
            logging.info('Loading dataset to memory...')
            audio = Audio()
            logging.info('Loading metadata...')
            audio.load_metadata()
            if len(argv) > 2 and argv[2] == 'preloaded':
                logging.info(f'Loading {c.DEFAULT_FEATURE} features...')
                audio.get_features(c.DEFAULT_FEATURE, preloaded=True)
                logging.info('Done.')
            else:
                logging.info('Extracting features from wav files...')
                audio.get_features('mel_spectrogram', preloaded=False)
                audio.get_features('spectrogram', preloaded=False)
                audio.get_features('mfcc', preloaded=False)




            print('Done!')
        elif argv[2] == 'serialize':
            if len(argv) > 2:
                if 'n' in argv[2]:
                    SERIALIZE_NORMALIZE = True
