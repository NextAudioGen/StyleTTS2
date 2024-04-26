# import os
# from sys import platform
# from setuptools import setup, find_packages

# with open('requirements.txt') as f:
#     required = f.read().splitlines()

# setup(
#    name='StyleTTS2',
#    version='2.0',
#    description='A text-to-speech (TTS) model that leverages style diffusion and adversarial training with large speech language models (SLMs) to achieve human-level TTS synthesis.',
#    license='MIT',
#    package_dir={'styletts2':'./'},
#    long_description=open('README.md').read(),
#    install_requires=required,
#    url="https://github.com/NextAudioGen/StyleTTS2.git",
# #    include_package_data=True,
#     package_data={
#         'styletts2': ['**/*.txt', '**/*.t7', '**/*.pth', '**/*.json', '**/*.yaml', '**/*.yml']
#     }

   
# )

import os
from setuptools import setup, find_packages

# Reading requirements from requirements.txt
with open('requirements.txt') as f:
    required = f.read().splitlines()

# Reading the long description from README.md
with open('README.md', 'r') as readme_file:
    long_description = readme_file.read()

setup(
    name='StyleTTS2',
    version='2.0',
    description='A text-to-speech (TTS) model that leverages style diffusion and adversarial training with large speech language models (SLMs) to achieve human-level TTS synthesis.',
    license='MIT',
    # Specify the package directory mapping
    package_dir={'styletts2': './'},  # Map 'styletts2' to the root directory
    packages=['styletts2'],  # Define the package to include
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=required,
    url="https://github.com/NextAudioGen/StyleTTS2.git",
    include_package_data=True,  # Ensuring all data files are included
    package_data={
        'styletts2': ['**/*.txt', '**/*.t7', '**/*.pth', '**/*.json', '**/*.yaml', '**/*.yml']
    },
)

