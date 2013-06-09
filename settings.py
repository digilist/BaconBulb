import sfml as sf

windowWidth = 800
windowHeight = 610

speedIncrement = 100

defaultFont = sf.Font.from_file("Ubuntu-R.ttf")
monospaceFont = sf.Font.from_file("DroidSansMono.ttf")

music = sf.Music.from_file("assets/chibi.ninja.ogg")
music.loop = True