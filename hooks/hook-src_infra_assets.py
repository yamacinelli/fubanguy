from PyInstaller.utils.hooks import collect_data_files

# Coleta todos os arquivos dentro de infra/assets/sounds
datas = collect_data_files('src.infra.assets.sounds')

# Coleta todos os arquivos dentro de infra/assets/fonts
datas += collect_data_files('src.infra.assets.fonts')

# Coleta todos os arquivos dentro de infra/assets/image
datas += collect_data_files('src.infra.assets.image')
