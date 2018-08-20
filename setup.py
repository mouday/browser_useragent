import setuptools
import os
import requests


# 将markdown格式转换为rst格式
def md_to_rst(from_file, to_file):
    r = requests.post(url='http://c.docverter.com/convert',
                      data={'to': 'rst', 'from': 'markdown'},
                      files={'input_files[]': open(from_file, 'rb')})
    if r.ok:
        with open(to_file, "wb") as f:
            f.write(r.content)


md_to_rst("README.md", "README.rst")

long_description = 'Add a fallback short description here'
if os.path.exists('README.rst'):
    long_description = open('README.rst', encoding="utf-8").read()

setuptools.setup(
    name="browser_useragent",
    version="0.0.1",
    author="Peng Shiyu",
    license='MIT License',
    author_email="pengshiyuyx@gmail.com",
    description="get a browser user_agent by random",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/mouday/browser_useragent",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[],  # 常用
    # include_package_data=True,  # 自动打包文件夹内所有数据
)
