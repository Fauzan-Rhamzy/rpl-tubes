#Sebelum run
    Hapus folder env (bukan file .env)
    Run di cmd, command ini 'python -m venv env' untuk virtual environment
    Terus run command ini "env\Scripts\activate" buat aktifin virtual environment, fungsinya biar semua dependensi diinstall di folder project ini
    Terus run command ini "pip install -r requirements.txt" ini buat install depensensinya
    Terus kalo semisal ada problem di importnya di vscode coba pencet shortcut ctrl+shift+p -> cari Python: Select Interpreter -> pilih python yang ('env':venv)

#Buat connection ke database
    cek file ".env"

#Run di vscode
kalo gabisa run pake f5/tombol run di vscode ketik di terminal aja 'flask run'
