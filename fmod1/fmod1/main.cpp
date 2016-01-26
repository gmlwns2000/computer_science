//
//  main.cpp
//  fmod1
//
//  Created by Hee Jun Lee on 1/21/16.
//  Copyright (c) 2016 Hee Jun Lee. All rights reserved.
//

#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <ncurses.h>
#include "inc/fmod.hpp"
#include "inc/fmod_errors.h" // Only if you want error checking

#define ERRCHECK(_result) ERRCHECK_fn(_result, __FILE__, __LINE__)

void (*Common_Private_Error)(FMOD_RESULT, const char *, int);
void Common_Fatal(const char *format, ...);

void ERRCHECK_fn(FMOD_RESULT result, const char *file, int line)
{
    if (result != FMOD_OK)
    {
        if (Common_Private_Error)
        {
            Common_Private_Error(result, file, line);
        }
        Common_Fatal("%s(%d): FMOD error %d - %s", file, line, result, FMOD_ErrorString(result));
    }
}

void Common_Fatal(const char *format, ...)
{
    char error[1024];
    
    va_list args;
    va_start(args, format);
    vsnprintf(error, 1024, format, args);
    va_end(args);
    error[1023] = '\0';
    
    printf("A fatal error has occurred...");
    printf("");
    printf("%s", error);
    
    exit(-1);
}

bool IsTerminalAvailable = false;

int main(int argc, const char * argv[]) {
    // insert code here...
    
    for (int argi = 1; argi < argc; argi++)
    {
        if (strcmp(argv[argi], "--debug-in-terminal") == 0)
        {
            printf("Debugging in terminal enabled\n");
            getchar(); // Without this call debugging will be skipped
            break;
        }
    }
    
    char *term = getenv("TERM");
    
    IsTerminalAvailable = (term != NULL);
    
    if (IsTerminalAvailable)
        IsTerminalAvailable = (initscr() != NULL);
    
    // Do some code here....
    
    if (IsTerminalAvailable)
    {
        printw("Press any key to exit...");
        refresh();
        
        getch();
        
        endwin();
    }
    
    bool exit = false;
    
    FMOD::System     *system;
    FMOD::Sound      *sound;
    FMOD::Channel    *channel = 0;
    FMOD_RESULT       result;
    unsigned int      version;
    void             *extradriverdata = 0;
    
    std::cout << "Hello, World!\n";
    
    result = FMOD::System_Create(&system);
    ERRCHECK(result);
    
    result = system->getVersion(&version);
    ERRCHECK(result);
    
    if (version < FMOD_VERSION)
    {
        Common_Fatal("FMOD lib version %08x doesn't match header version %08x", version, FMOD_VERSION);
    }
    
    result = system->init(32, FMOD_INIT_NORMAL, extradriverdata);
    ERRCHECK(result);
    
    result = system->createSound("/Users/19hlee/desktop/git/test.mp3", FMOD_DEFAULT, 0, &sound);
    ERRCHECK(result);
    
    result = sound->setMode(FMOD_LOOP_OFF);    /* drumloop.wav has embedded loop points which automatically makes looping turn on, */
    ERRCHECK(result);                           /* so turn it off here.  We could have also just put FMOD_LOOP_OFF in the above CreateSound call. */
    result = system->playSound(sound, 0, false, &channel);
    ERRCHECK(result);
    
    unsigned int pos = 0;
    
    do {
        result = system->update();
        ERRCHECK(result);
        result = channel->getPosition(&pos, FMOD_TIMEUNIT_MS);
        ERRCHECK(result);
        printf("%fs\n",(float)pos/1000);
    } while (!exit);
    
    printf("Exit");
    return 0;
}
