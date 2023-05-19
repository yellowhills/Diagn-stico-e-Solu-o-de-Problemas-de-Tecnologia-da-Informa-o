from PIL import Image
episodios = Image.open('general.png')
tamanho = (720,1280) 
episodios_redimensionada = episodios.resize(tamanho)
episodios_redimensionada.save('',optmize=True,quality=100)

largura_original,altura_original = episodios.size
nova_largura = 720
nova_altura = int(altura_original*(nova_largura/largura_original))
tamanho = (nova_largura,nova_altura)