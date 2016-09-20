# -*- coding: utf-8 -*-

# POLIMORFISMO: Diferentes Comportamentos - de cada método.
# Para entender Polimorifsmo, vamos utilizar um programa que reproduz arquivos de áudio

# Para descomprimir um arquivo e áudio é diferente para cada tipo de arquivo (.wav, .mp3, .wma, .ogg, são exemplos).
# Então a ideia é criar uma classe AudioFile e 3 subclasses (MPFile, WavFile e OggFile) e cada subclasse implementa um método play de acordo com a sua extensão.

class AudioFile:
	def __init__(self, filename):
		'''Se o arquivo tiver uma extensão diferente da extensão esperada (mp3, wav ou ogg), gera uma exceção'''
		if not filename.endswith(self.ext):
			raise Exception("Invalid file format!")

		self.filename = filename

class MP3File(Audiofile):
	ext = "mp3"
	def play(self):
		print("Playing {} as mp3".format(self.filename))

class WavFile(Audiofile):
	ext = "wav"
	def play(self):
		print("Playing {} as wav".format(self.filename))

class OggFile(Audiofile):
	ext = "ogg"
	def play(self):
		print("Playing {} as ogg".format(self.filename))

# Criar o objeto mp3 e executa método play específico para a subclasse MP3File
mp3 = MP3File("myfile.mp3")
mp3.play()
# playing myfile.mp3 as mp3

# Criar o objeto wav e executa método play específico para a subclasse WavFile
wav = WavFile("myfile.wav")
wav.play()
# playing myfile.wav as wav

# Criar o objeto ogg e executa método play específico para a subclasse OggFile
ogg = OggFile("myfile.ogg")
ogg.play()
# playing myfile.ogg as ogg

# Se criarmos um objeto que tenha extensão errada, a exceção é executada.
not_an_ogg = OggFile("notnot.not")
# Exception: Invalid file format!