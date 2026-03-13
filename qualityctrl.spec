# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec — QualityCtrl Muayene Sistemi
# Çalıştır: pyinstaller qualityctrl.spec

from PyInstaller.utils.hooks import collect_data_files, collect_submodules

block_cipher = None

# ── Gizli import'lar ──────────────────────────────────────────────────────────
hidden = [
    # uvicorn
    'uvicorn.logging',
    'uvicorn.loops', 'uvicorn.loops.auto', 'uvicorn.loops.asyncio',
    'uvicorn.protocols',
    'uvicorn.protocols.http', 'uvicorn.protocols.http.auto',
    'uvicorn.protocols.http.h11_impl',
    'uvicorn.protocols.websockets', 'uvicorn.protocols.websockets.auto',
    'uvicorn.lifespan', 'uvicorn.lifespan.on', 'uvicorn.lifespan.off',
    # anyio / asyncio
    'anyio', 'anyio._backends._asyncio',
    # fastapi / starlette
    'fastapi', 'starlette', 'starlette.routing', 'starlette.staticfiles',
    # pydantic
    'pydantic', 'pydantic.deprecated.class_validators',
    # aiosqlite
    'aiosqlite',
    # aiofiles
    'aiofiles', 'aiofiles.os', 'aiofiles.threadpool',
    # multipart
    'multipart',
    # pywebview
    'webview', 'webview.platforms.winforms',
    # pythonnet (pywebview Windows backend)
    'clr',
]
hidden += collect_submodules('uvicorn')
hidden += collect_submodules('starlette')
hidden += collect_submodules('fastapi')

# ── Veri dosyaları ────────────────────────────────────────────────────────────
datas = [
    # Frontend (HTML + JS + CSS)
    ('frontend', 'frontend'),
    # SQL şema
    ('backend/database/schema.sql', 'backend/database'),
]

a = Analysis(
    ['launcher.py'],
    pathex=['.'],
    binaries=[],
    datas=datas,
    hiddenimports=hidden,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tkinter', 'matplotlib', 'numpy', 'pandas', 'PIL'],
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
    name='QualityCtrl',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,          # pencere uygulaması — siyah konsol çıkmaz
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,              # ikon eklemek istersen: icon='icon.ico'
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='QualityCtrl',     # dist/QualityCtrl/ klasörüne çıkar
)
