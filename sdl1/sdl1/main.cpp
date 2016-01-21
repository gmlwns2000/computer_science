//Using SDL and standard IO
#include <stdio.h>
#include <SDL2/SDL.h>
#include <SDL2_image/SDL_image.h>

#include "Essential.h"

//Screen dimension constants
const int SCREEN_WIDTH = 640;
const int SCREEN_HEIGHT = 380;

bool init();
bool loadMedia();
void close();

SDL_Window* g_Window = NULL;
SDL_Surface* g_ScreenSurface = NULL;
SDL_Surface* spr_logo = NULL;
char path_logobmp[] = "data/preview.bmp";

bool init()
{
    bool success = true;
    if( SDL_Init( SDL_INIT_VIDEO | SDL_INIT_AUDIO ) < 0 )
    {
        printf( "SDL could not initialize! SDL_Error: %s\n", SDL_GetError() );
        success = false;
    }
    else
    {
        g_Window = SDL_CreateWindow( "mp3 player", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN );
        if( g_Window == NULL )
        {
            printf( "Window could not be created! SDL_Error: %s\n", SDL_GetError() );
            success = false;
        }
        else
        {
            
        }
    }
    
    return success;
}

bool loadMedia()
{
    bool success = true;
    spr_logo = SDL_LoadBMP( path_logobmp );
    if( spr_logo == NULL )
    {
        printf( "Unable to load image %s! SDL Error: %s\n", path_logobmp, SDL_GetError() );
        success = false;
    }
    
    return success;
}

void close()
{
    //Free Sprites
    SDL_FreeSurface( spr_logo );
    spr_logo = NULL;
    //Free Window
    SDL_DestroyWindow( g_Window );
    g_Window = NULL;
    SDL_Quit();
}

int main( int argc, char* args[] )
{
    printlog("strart program");
    if( !init() )
    {
        printlog( "Failed to initialize!\n" );
    }
    else
    {
        printlog("SDL init success");
        if( !loadMedia() )
        {
            printlog( "Failed to load media!\n" );
        }
        else
        {
            printlog("SDL Load data succcess");
            bool quit = false;
            SDL_Event e;
            while( !quit )
            {
                while( SDL_PollEvent( &e ) != 0 )
                {
                    if( e.type == SDL_QUIT )
                    {
                        quit = true;
                    }
                    //User presses a key
                    else if( e.type == SDL_KEYDOWN )
                    {
                        //Select surfaces based on key press
                        switch( e.key.keysym.sym )
                        {
                            case SDLK_UP:
                                printlog("up");
                                break;
                            case SDLK_DOWN:
                                break;
                            default:
                                break;
                        }
                    }
                }
                
                SDL_BlitSurface( spr_logo, NULL, g_ScreenSurface, NULL );
                
                SDL_UpdateWindowSurface( g_Window );
            }
        }
    }
    
    close();
    
    return 0;
}