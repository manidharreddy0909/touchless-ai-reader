# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files

datas = [('venv\\Lib\\site-packages\\mediapipe', 'mediapipe'), ('venv\\Lib\\site-packages\\mediapipe\\modules', 'mediapipe\\modules')]
datas += collect_data_files('mediapipe')


a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=['mediapipe', 'mediapipe.python', 'mediapipe.python.solutions', 'mediapipe.python.solutions.hands', 'mediapipe.python.solutions.face_mesh'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='TouchlessAIReader',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
