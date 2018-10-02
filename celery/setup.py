from setuptools import find_packages, setup

setup(
    name='worker',
    packages=find_packages(),
    install_requires=['celery[redis]', 'sqlalchemy', 'psycopg2-binary'],
    entry_points={
        'console_scripts': [
            'worker = testapp.worker:main',
            'client = testapp.client:main',
        ],
    }
)
