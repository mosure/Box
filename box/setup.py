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
        'authlib',
        'flask>=1.1.1',
        'flask-bcrypt',
        'flask-injector',
        'flask-marshmallow',
        'neo4j-driver',
        'python-dotenv'
    ],
    zip_safe=False
)
