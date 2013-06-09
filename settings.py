import sfml as sf

windowWidth = 800
windowHeight = 610

speedIncrement = 100

defaultFont = sf.Font.from_file("Ubuntu-R.ttf")
monospaceFont = sf.Font.from_file("DroidSansMono.ttf")

monsterTexture = sf.Texture.from_file("assets/monster.png")

music = sf.Music.from_file("chibi.ninja.ogg")