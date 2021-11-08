import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ML_toolbox',
    version='0.0.1',
    author='Mathew Varghese',
    author_email='mathewv@uw.edu',
    description='Some functions for plotting images',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mathewvarghesemanu/ML_toolbox',
    project_urls = {
        
    },
    license='MIT',
    packages=['ML_toolbox'],
    install_requires=['opencv-python, matplotlib, numpy'],
)