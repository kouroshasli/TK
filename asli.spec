# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['run_server.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('templates', 'templates'),
        ('static', 'static'),
        ('locale', 'locale'),
        ('manage.py', '.'),
        ('requirements.txt', '.'),
        ('db.sqlite3', '.'),
        ('main', 'main'),
        ('kouroshasli', 'kouroshasli'),
    ],
    hiddenimports=['django.core.management', 'django.core.management.commands.runserver'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='asli',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)
