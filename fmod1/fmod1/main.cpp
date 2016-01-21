//
//  main.cpp
//  fmod1
//
//  Created by Hee Jun Lee on 1/21/16.
//  Copyright (c) 2016 Hee Jun Lee. All rights reserved.
//

#include <iostream>
#include "inc/fmod.hpp"
#include "inc/fmod_errors.h" // Only if you want error checking

typedef FMOD::Sound* SoundClass;

class SoundSystemClass
{
private:
    
public:
    // Pointer to the FMOD instance
    FMOD::System *m_pSystem;
    FMOD::ChannelGroup *m_pChannelGroup;
    
    void Initialize ()
    {
        if (FMOD::System_Create(&m_pSystem) != FMOD_OK)
        {
            // Report Error
            printf("system creat ERROR\n");
            return;
        }
        
        int driverCount = 0;
        m_pSystem->getNumDrivers(&driverCount);
        
        if (driverCount == 0)
        {
            // Report Error
            printf("NONE DRIVERS\n");
            return;
        }
        
        // Initialize our Instance with 36 Channels
        m_pSystem->init(36, FMOD_INIT_NORMAL, NULL);
        printf("Init success\n");
    }
    
    void createSound(SoundClass *pSound, const char* pFile)
    {
        m_pSystem->createSound(pFile, FMOD_DEFAULT, 0, pSound);
    }
    
    void playSound(SoundClass pSound, bool bLoop = false)
    {
        if (!bLoop)
            pSound->setMode(FMOD_LOOP_OFF);
        else
        {
            pSound->setMode(FMOD_LOOP_NORMAL);
            pSound->setLoopCount(-1);
        }
        
        m_pSystem->playSound(pSound, NULL, false, 0);
    }
    
    void releaseSound(SoundClass pSound)
    {
        pSound->release();
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    // Initialize our sound system
    SoundSystemClass sound;
    sound.Initialize();
    
    // Create a sample sound
    SoundClass soundSample;
    printf("start\n");
    sound.createSound(&soundSample, "test.mp3");
    
    // Play the sound, with loop mode
    sound.playSound(soundSample, true);
    
    // Do something meanwhile...
    
    for(int i=0;i<10000000;i++){
        printf("%d\n",i);
    }
    
    printf("12\n");
    // Release the sound
    sound.releaseSound(soundSample);
    printf("EXIT\n");
    return 0;
}
