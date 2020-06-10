from setuptools import setup

setup(
    name='sports_analytics',
    packages=['calc_stats_api', 'initialize_db'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)