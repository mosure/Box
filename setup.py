from setuptools import setup


setup(
    name='box',
    version='1.0',
    description='Box Box API',
    url='http://github.com/mosure/box',
    author='Sudo.X',
    author_email='admin@sudox.dev',
    license='',
    packages=['box'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask-injector'
    ],
    zip_safe=False
)
