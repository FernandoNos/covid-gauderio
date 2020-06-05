import setuptools

setuptools.setup(name='CoviTche',
      version='1.0',
      description='Covid updates',
      author='Fernando Nos',
      author_email='nosfernandos@gmail.com',
      packages=setuptools.find_packages(),
      install_requires=["tweepy","requests","apscheduler"]
     )
