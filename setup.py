from setuptools import setup, find_packages

setup(name='mnist-recognizer',
      version='0.1',
      packages=find_packages(),
      description='MNIST CNN',
      author='Hariel Giacomuzzi',
      author_email='hariel.dias@acad.pucrs.br',
      license='MIT',
      install_requires=[
          'keras',
          'h5py'
      ],
      zip_safe=False)