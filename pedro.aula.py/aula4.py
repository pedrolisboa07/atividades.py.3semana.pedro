def calcular_media (notas):
#retorna a media.
   t = sum(notas)
   return t / len(notas)
minhas_notas =[9.5, 7.0,9.0,6.5]
media_final = calcular_media(minhas_notas)
print(f"A media das notas é: {media_final:2f}")
print ("\n--- Documentação da função(docstring)---")
print (calcular_media.__doc__)