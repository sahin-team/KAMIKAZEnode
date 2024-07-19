from setuptools import find_packages, setup

package_name = 'kamikaze'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='al-tair',
    maintainer_email='tahnazali@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'coordinate = kamikaze.coordinate:main',
            'data = kamikaze.data:main',
            'datatest = kamikaze.data_test:main',
            'kamikazeOn = kamikaze.kamikazeBaslangicZamani:main',
            'kamikazeOff = kamikaze.kamikazeBitisZamani:main',
            'orientation = kamikaze.orientation:main',
            'QRcoordinate = kamikaze.qr_coordinate:main',
            'QRcotest = kamikaze.qrcoordinate_test:main',
            'redzone = kamikaze.red_zone:main',
            'redzonetest = kamikaze.redzone_test:main',
            'controler = kamikaze.ControlCommand:main',
            'kamikazecompleted = kamikaze.KamikazeCompleted:main',
        ],
    },
)
