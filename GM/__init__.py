#!/usr/bin/env python
#! coding: utf-8
#! python3
# Python ish game layer à la GM
# Dirty as hay, if you learn python with this file, you will learn garbage.
# 2022

import random
import os.path
import pygame
import pygame.freetype


#===== Variable Functions =====
#===== Asset Management =====
#----- Assets And Tags -----
#----- Animation Curves -----
#----- Sprites -----
#----- Tile Sets -----
#----- Audio -----
#----- Paths -----
#----- Scripts -----
#----- Shaders -----
#----- Sequences -----
#----- Fonts -----

_internal_fonts = []

def font_add( name=None, size=16, bold=False, italic=False, first=32, last=128 ) :
	global _internal_fonts
	
	# Size sanity check
	size = int( size )
	if size < 1 : size = 1
	
	# Font file check
	if name != None :
		if not os.path.exists( name ) :
			print( f"Can't find file '{name}', fall back to default font." )
			name = None
	
	# Load it
	if name != None :
		# font = pygame.freetype.Font( name, size )
		font = pygame.font.Font( name, size )
	else :
		font = pygame.font.SysFont( None, size )
	
	_internal_fonts.append( font )
	return font

#----- Timelines -----
#----- Objects -----
#----- Instances -----
#----- Rooms -----

#===== General Game Control =====
game_id = 0
game_save_id = game_id
game_display_name = "Great Mishmash"
game_project_name = "Undefined"

#
def game_end() :
	pygame.quit()

#
def game_restart(  ) :
	pass

#
def game_load(  ) :
	pass

#
def game_load_buffer(  ) :
	pass

#
def game_save(  ) :
	pass

#
def game_save_buffer(  ) :
	pass

#
def game_get_speed(  ) :
	pass

#
def game_set_speed(  ) :
	pass

#
def highscore_add() :
	pass

#
def highscore_name() :
	pass

#
def highscore_value() :
	pass

#
def highscore_clear() :
	pass

#
def draw_highscore() :
	pass

#
def cursor_sprite() :
	pass



#===== Movement And Collisions =====
#===== Drawing =====
_draw_surface_currentSurface = None

#----- Colour And Alpha -----

c_aqua = (0,255,255)
c_black = (0,0,0)
c_blue = (0,0,255)
c_dkgray = (64,64,64)
c_fuchsia = (255,0,255)
c_gray = (128,128,128)
c_green = (0,128,0)
c_lime = (0,255,0)
c_ltgray = (192,192,192)
c_maroon = (128,0,0)
c_navy = (0,0,128)
c_olive = (128,128,0)
c_orange = (64,160,0)
c_purple = (128,0,128)
c_red = (255,0,0)
c_silver = (192,192,192)
c_teal = (0,128,128)
c_white = (255,255,255)
c_yellow = (255,255,0)

_draw_color_currentColor = c_black
_draw_color_currentAlpha = 1

#
def colour_get_blue() :
	pass

#
def colour_get_green() :
	pass

#
def colour_get_red() :
	pass

#
def colour_get_hue() :
	pass

#
def colour_get_saturation() :
	pass

#
def colour_get_value() :
	pass

#
def draw_getpixel() :
	pass

#
def draw_getpixel_ext() :
	pass

#
def draw_get_colour() :
	pass

#
def draw_get_alpha() :
	pass

#
def make_colour_hsv() :
	pass

#
def make_colour_rgb( r=0, g=0, b=0) :
	return (r,g,b)

#
def merge_colour() :
	pass

#
def draw_clear( color=(0,0,0) ) :
	global _draw_surface_currentSurface
	_draw_surface_currentSurface.fill( color )

#
def draw_clear_alpha() :
	pass

#
def draw_set_alpha( alpha=0 ) :
	global _draw_color_currentAlpha
	_draw_color_currentAlpha = alpha

#
def draw_set_color( color=(0,0,0) ) :
	global _draw_color_currentColor
	_draw_color_currentColor = color

#Non standard GM
def sanitize_color( color=None ):
	
	if color == None : color = 0
	
	# string families (Hex and HTML)
	if isinstance( color, str ) :
		#TODO: scan for $ or # for hex color, and maybe some html names
		color = (0,0,0)
	
	# RGB integer
	if isinstance( color, int ) :
		make_color_rgb( (color % 256), ((color/256)%256), ((color/65536)%256) )
	
	# multiple values
	if isinstance( color, tuple ) or isinstance( color, list ) :
		if len( color ) not in [3,4] :
			color = (0,0,0)
	
	return color


#----- GPU Control -----
#----- Mipmapping -----
#----- Basic Forms -----
#----- Sprites And Tiles -----
#----- Text -----
fa_left = "left"
fa_center = "center"
fa_right = "right"
fa_top = "top"
fa_middle = "middle"
fa_bottom = "bottom"

_draw_text_currentFont = None
_draw_text_hAlign = fa_left
_draw_text_vAlign = fa_top

#
def draw_set_font( font=None ) :
	global _internal_fonts
	global _draw_text_currentFont
	
	if font not in _internal_fonts : font = _internal_fonts[0]
	
	_draw_text_currentFont = font
	

#
def draw_set_halign( halign=fa_left ) :
	global _draw_text_hAlign
	
	if halign not in [fa_left, fa_center, fa_right] :
		halign = fa_left
	
	_draw_text_hAlign = halign
	

#
def draw_set_valign( valign=fa_top ) :
	global _draw_text_vAlign
	
	if valign not in [fa_top, fa_middle, fa_bottom] :
		valign = fa_top
	
	_draw_text_vAlign = valign
	

#
def draw_get_font( ) :
	global _draw_text_currentFont
	return _draw_text_currentFont

#
def draw_get_halign( ) :
	global _draw_text_hAlign
	return _draw_text_hAlign

#
def draw_get_valign( ) :
	global _draw_text_vAlign
	return _draw_text_vAlign


#
def draw_text( coords=(0,0), string="Text" ) :
	draw_text_color( coords, string, _draw_color_currentColor, _draw_color_currentAlpha )

#
def draw_text_ext( ) :
	pass

#
def draw_text_color( coords=(0,0), string="Text", colors=( c_black, c_black, c_white, c_white), alpha=0.5 ) :
	global _draw_surface_currentSurface
	global _draw_text_currentFont
	global _draw_text_hAlign
	global _draw_text_vAlign
	
	error = None
	
	# Normalization and sanity checks
	
	if _draw_surface_currentSurface == None : error = "No surface"
	if _draw_text_currentFont == None : error = "No Font"
	
	if isinstance( coords, tuple ) or isinstance( coords, list ) :
		x,y = coords
	else :
		error = "Malformed coords"
	
	if not isinstance( string, str ) :
		string = str( string )
	
	if isinstance( colors, tuple ) or isinstance( colors, list ) :
		#TODO Better check. Use sanitize_color()
		if len( colors ) == 3 :
			c = colors
			colors = (c,c,c,c)
		
	
	
	if error == None :
		
		textImage = _draw_text_currentFont.render( string, False, colors[0])
		
		# Compute coordinates
		if _draw_text_hAlign == fa_center :
			w,h = textImage.get_size()
			x -= w/2
		
		if _draw_text_hAlign == fa_right :
			w,h = textImage.get_size()
			x += w
		
		if _draw_text_vAlign == fa_middle :
			w,h = textImage.get_size()
			y -= h/2
		
		if _draw_text_vAlign == fa_bottom :
			w,h = textImage.get_size()
			y += h
		
		_draw_surface_currentSurface.blit( textImage, (x,y) )
		
	else :
		print( error )
	

#
def draw_text_transformed( ) :
	pass

#
def draw_text_ext_colour( ) :
	pass

#
def draw_text_ext_transformed( ) :
	pass

#
def draw_text_transformed_colour( ) :
	pass

#
def draw_text_ext_transformed_colour( ) :
	pass


#----- Primitives And Vertex Formats -----
#----- Surfaces -----

_internal_surfaces = []

#
def surface_exists() :
	pass

# Creates a surface of the indicated width and height.
# Returns the id of the surface, which must be used in all further calls.
# Note that the surface will not be cleared. 
def surface_create( size=(128,128) ) :
	return surface_create_ext( size, color=None, mode=pygame.SRCALPHA )

#
def surface_create_ext( size=(128,128), color=None, mode=pygame.SRCALPHA ) :
	global _internal_surfaces
	
	surface = pygame.Surface( size, mode )
	_internal_surfaces.append( surface )
	
	if color != None :
		surface_set_target( surface )
		draw_clear( color )
		surface_reset_target()
	
	return surface

#
def surface_resize() :
	pass

#
def surface_set_target( surface=None ) :
	global _internal_surfaces
	global _draw_surface_currentSurface
	
	if surface not in _internal_surfaces : surface = _internal_surfaces[0]
	
	_draw_surface_currentSurface = surface
	


# Resets the drawing target to the normal screen.
def surface_reset_target() :
	global _internal_surfaces
	global _draw_surface_currentSurface
	
	_draw_surface_currentSurface = _internal_surfaces[0]
	

#----- Lighting -----
#----- Particles -----
#----- Textures -----
#----- Shaders -----
#----- Video Playback -----
#===== Cameras And Display =====
#===== Game Input =====
#===== Data Structures =====
#===== Strings =====
#===== Maths And Numbers =====
#===== Physics =====
#===== Asynchronous Functions =====
#===== Networking =====
#===== File Handling =====
#===== Buffers =====
#===== Debugging =====
#===== Garbage Collection =====

# Miscelaneous

# Choose one item of a list at random
def choose( l=None ) :
	r = None
	if l != None :
		r = l[ random.randrange( 0, len(l) ) ]
	return r


# Initialisation
if __name__!="__main__":
	WINDOW_SIZE = (800,600)
	
	# Initialize
	pygame.init()
	pygame.mixer.init()
	clock = pygame.time.Clock()
	
	surface_create( WINDOW_SIZE )
	_internal_surfaces[0] = pygame.display.set_mode( WINDOW_SIZE )
	surface_set_target()
	
	_draw_text_currentFont = font_add()

