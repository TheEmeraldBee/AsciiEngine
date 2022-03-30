import os
import sys
import pygame

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "CUSTOM_SUPPORT_PROMPT"

from asciiEngine.constants import *
from asciiEngine.window import *
from asciiEngine.time import *

print(SUPPORTMESSAGE)

# Clean up imports
del os, sys, pygame
