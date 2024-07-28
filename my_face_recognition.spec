# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['my_face_recognition.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('virtual_environments\\face_app_env\\Lib\\site-packages\\face_recognition_models\\models\\dlib_face_recognition_resnet_model_v1.dat', 'face_recognition_models/models'),
        ('virtual_environments\\face_app_env\\Lib\\site-packages\\face_recognition_models\\models\\mmod_human_face_detector.dat', 'face_recognition_models/models'),
        ('virtual_environments\\face_app_env\\Lib\\site-packages\\face_recognition_models\\models\\shape_predictor_5_face_landmarks.dat', 'face_recognition_models/models'),
        ('virtual_environments\\face_app_env\\Lib\\site-packages\\face_recognition_models\\models\\shape_predictor_68_face_landmarks.dat', 'face_recognition_models/models'),
        ('Images', 'Images')
    ],
    hiddenimports=[
        'face_recognition',
        'cv2',
        'MySQLdb',
        'sqlalchemy',
        'dotenv',
        'numpy',
        'datetime'
    ],
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
    name='my_face_recognition',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    icon='icon.ico',
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
