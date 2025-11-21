# Exercíci 021
''' Faça um programa em python que abra e reproduza o áudio de um arquivo MP3. '''

# importando biblioteca
import pygame

# inicialização do pygame
pygame.init()

# Carregando aquivo mp3
pygame.mixer.music.load('atv21.mp3')

# inicia a reprodução
pygame.mixer.music.play()

# Matém a reprodução do arquivo até seu término
input()
pygame.event.wait()
