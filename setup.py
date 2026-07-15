from setuptools import setup, find_packages

setup(
    name='visevent-eval',
    version='0.1.0',
    description='Python evaluation toolkit for VisEvent SOT Benchmark',
    author='Codex',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy>=1.18.0',
        'matplotlib>=3.0.0'
    ],
    entry_points={
        'console_scripts': [
            'visevent-eval=visevent_eval.evaluator:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
