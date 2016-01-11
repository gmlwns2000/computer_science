#include "SDL2/SDL.h"
#include <stdio.h>

const int SCREEN_WIDTH = 640;
const int SCREEN_HIEGHT = 420;

int main( int argc, char* args[] )
{
	printf("Hello, World!\n");    
	SDL_Window* window = NULL;
	SDL_Surface* screenSurface = NULL;
	if( SDL_Init( SDL_INIT_VIDEO ) < 0 )
	{
		printf("SDL init fail. Detail: %s\n", SDL_GetError());
	}else{
		window = SDL_CreateWindow( "SDL TEST", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, SCREEN_WIDTH,
						SCREEN_HIEGHT, SDL_WINDOW_SHOWN);
		if(window==NULL){
			printf("SDL window init fail / Detail: %s\n", SDL_GetError());
		}else{
			screenSurface = SDL_GetWindowSurface( window );
			SDL_FillRect( screenSurface, NULL, SDL_MapRGB( screenSurface->format, 0xFF, 0xFF, 0xFF ) );
			SDL_UpdateWindowSurface( window );
			SDL_Delay( 2000 );
			SDL_DestroyWindow( window );
			SDL_Quit();
		}
	}
	return 0;
}
