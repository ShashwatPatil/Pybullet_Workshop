from setuptools import setup

setup(name='gym_line_follower',
      version='0.1.2',
      install_requires=['gym',
                        'pybullet', 'opencv-python', 'shapely==1.8.5', 'numpy', 'scipy','opencv-contrib-python==4.6.0.66'],
      author="Nejc Planinsek",
      author_email="planinseknejc@gmail.com",
      description="Line follower simulator environment.",
      )
