__author__ = 'Yaoza'
import pygame
import os
import constants


class ImageLoader():

    def __init__(self):
        pygame.init()

        # print "create new screen"
        self.screen = pygame.display.set_mode((1024,768), pygame.FULLSCREEN)

        pygame.mouse.set_visible(0)
        self.black = pygame.image.load(constants.IMAGE_DIR + "black.png")

        self.file_number = ""
        self.file_prefix = ""
        self.file_suffix = ""
        self.next_file = True

    def __del__(self):
        pygame.quit()

    def set_image(self, image_path):
        self.image = pygame.image.load(image_path)
        filename = image_path[image_path.rfind("/")+1:]
        self.current_path = image_path[:image_path.rfind("/")+1]
        # print("filename", filename.split())
        self.file_number = ""
        self.file_prefix = ""
        self.file_suffix = ""
        numbers_found = False
        for character in list(filename):
            # print("character:", character)
            if character.isdigit():
                numbers_found = True
                self.file_number += character
            else:
                if numbers_found:
                    self.file_suffix += character
                else:
                    self.file_prefix += character

        print("file number:", self.file_number)

    def load(self):
        # load the image
        self.screen.fill((255,255,255))
        self.screen.blit(self.image,(0,0))
        pygame.display.flip()
         # check if thre's a next file.  Should enter this once at least
        if self.next_file:
            if len(self.file_number) > 0:
                # number found
                file_number = str(int(self.file_number) + 1).zfill(len(self.file_number))
                new_file_spec = self.current_path + self.file_prefix + file_number + self.file_suffix

                if os.path.isfile(new_file_spec):
                    self.file_number = file_number
                    self.image = pygame.image.load(new_file_spec)
                    print("Setting new image:", new_file_spec)
                    self.next_file = True
                else:
                    print("Cannot find file:", new_file_spec)
                    self.next_file = False
            else:
                self.next_file = False

    def blank(self):
        self.screen.fill((255,255,255))
        self.screen.blit(self.black,(0,0))
        pygame.display.flip()

    def check_event(self):
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.type == pygame.QUIT:
                    self.quit()

    def quit(self):
        pygame.quit()
