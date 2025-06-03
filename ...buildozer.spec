[app]
title = FinancialCalculator
package.name = Financial_Calculator
package.domain = kr.co.fahub
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
# source.include_patterns = font/*,images/*.png
source.exclude_exts = spec,txt
source.exclude_dirs = tests, bin, venv, __pycache__
version = 1.3.6
# requirements = python3,kivy==2.1.0,kivymd==1.0.1,sdl2_ttf,pillow,beautifulsoup4,soupsieve,requests,typing_extensions
requirements = python3==3.11.0,hostpython3==3.11.0,kivy==2.1.0,kivymd==1.0.1,cython==0.29.33,sdl2_ttf,pillow
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.permissions = android.permission.INTERNET,CCESS_NETWORK_STATE (name=android.permission.WRITE_EXTERNAL_STORAGE;maxSdkVersion=18)
android.api = 34
android.private_storage = True
android.archs = arm64-v8a
android.allow_backup = True
android.allow_cleartext_traffic = True
android.cmake_options = -DCMAKE_POLICY_VERSION_MINIMUM=3.5
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0
ios.codesign.allowed = false
[buildozer]
log_level = 0
warn_on_root = 1
