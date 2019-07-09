from setuptools import setup, find_packages


setup(
    name="midi-transposer",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "music21",
        "numpy",
        "matplotlib",
        "scipy",
        "argparse"
    ],
    entry_points={
        "console_scripts":
            "mtrans = transposer.main:main"
    },
    zip_safe=False,
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ],
)
