#!/usr/bin/env python
#! coding: utf-8
#! python3
# Game 2022

import random
import GM

#==============================================================================
# Main program
#==============================================================================

# Add a BIG font
bigFont = GM.font_add( None, 128 )
GM.draw_set_font( bigFont )
GM.draw_set_halign( GM.fa_center )
GM.draw_set_valign( GM.fa_middle )

# Variable to control the main loop
running = True
x = 0

# main loop
while running:
	
	# Event handling, gets all event from the event queue
	for event in GM.pygame.event.get():
		if event.type == GM.pygame.QUIT:
			running = False
		
	
	# Step
	x = random.randrange( -2, 2 )
	
	# Draw
	GM.draw_clear( GM.c_purple )
	
	# Text
	GM.draw_text_color( (400+x,300), "Hello!", GM.c_yellow )
	
	GM.pygame.display.flip()
	GM.clock.tick(60)
	GM.pygame.event.poll()
