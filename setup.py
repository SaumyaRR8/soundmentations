from setuptools import setup, find_packages

setup(
    name='soundmentations',
    version='0.1.0',
    author='Saumya Ranjan',
    author_email='saumyarr8@outlook.com',
    description='Sound augmentations for audio data',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies your package requires        
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)