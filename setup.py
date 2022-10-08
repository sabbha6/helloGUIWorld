from setuptools import setup

APP=['helloGUIWorld.py']
OPTIONS = {
    'argv_emulation' : True,
    'iconfile':'wave.png',
}
setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']
)
# pyinstaller my_script.py --onefile --windowed
# After this run the below cmds in terminal
# 'python setup.py py2app'
# Go to dist dir and get your app