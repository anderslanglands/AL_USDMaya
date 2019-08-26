name='alusdmaya'
version='0.31.1'

requires=['usd-19.05', 'maya-2019', 'gtest-2.8']

def commands():
    env.MAYA_PLUG_IN_PATH.append('{root}/plugin')
    env.PXR_PLUGINPATH_NAME.append('{root}/lib')
    env.LD_LIBRARY_PATH.append('{root}/lib')
    env.PYTHONPATH.append('{root}/lib/python')
