# -*- mode: python -*-
a = Analysis(['mediamochil.py'],
             pathex=['C:\\Users\\Zion\\PycharmProjects\\untitled'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='mediamochil.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='mediamochil')
