# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['..\\main.py'],
    pathex=[],
    binaries=[],
    datas=
    [
        ('D:/bachkhoa/bachkhoa222/Luan van/CompleteApplication/rehab_games/sprites/Bird/*.png', 'rehab_games/sprites/Bird/'),
        ('D:/bachkhoa/bachkhoa222/Luan van/CompleteApplication/rehab_games/sprites/Cactus/*.png', 'rehab_games/sprites/Cactus/'),
        ('D:/bachkhoa/bachkhoa222/Luan van/CompleteApplication/rehab_games/sprites/Dino/*.png', 'rehab_games/sprites/Dino/'),
        ('D:/bachkhoa/bachkhoa222/Luan van/CompleteApplication/rehab_games/sprites/Other/*.png', 'rehab_games/sprites/Other/'),
        ('D:/bachkhoa/bachkhoa222/Luan van/CompleteApplication/rehab_games/sprites/*.png', 'rehab_games/sprites/'),
        ('D:/bachkhoa/bachkhoa222/Luan van/CompleteApplication/rehab_games/sprites/*.jpeg', 'rehab_games/sprites/'),
        ('D:/bachkhoa/bachkhoa222/Luan van/CompleteApplication/rehab_games/Be_Vietnam_Pro/*', 'rehab_games/Be_Vietnam_Pro/'),
        ('D:/bachkhoa/bachkhoa222/Luan van/CompleteApplication/rehab_games/music/*', 'rehab_games/music/'),
        ('D:/bachkhoa/bachkhoa222/Luan van/CompleteApplication/lib/x64/LeapC*', 'lib/x64/'),
        ('D:/bachkhoa/bachkhoa222/Luan van/CompleteApplication/model/weights/*', 'model/weights/')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='bk_rehab',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='D:\\bachkhoa\\bachkhoa222\\Luan van\\CompleteApplication\\rehab_games\\sprites\\BK.png'
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='bk_rehab',
)