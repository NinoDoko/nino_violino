This is a README in progress. 

Basically, it's a program that makes its own music. 

Prerequisites - 
`python setup.py` - for a few packages that I run; most notably midiutil. 

Note: As of writing, this seems to have a bug that can be fixed by manually editing a file in the package. It's a bit dirty but basically a workaround. 
The entire article is here - https://cyberspy.io/articles/2017-10-29t150250-0400--maestro-cue-the-music/ ; it is unrelated to what this repo does but it does show us the fix (thanks for that!)
To fix the bug, do this: 

`vim /usr/lib/python2.7/site-packages/midiutil/MidiFile.py`

Find the line for the event NoteOff (in vim, you can use /elif event.type == 'NoteOff')

Replace the entire block with: 
```
elif event.type == 'NoteOff':
                if len(stack[str(event.pitch)+str(event.channel)]) > 1:
                    event.time = stack[str(event.pitch)+str(event.channel)].pop()
                    tempEventList.append(event)
                else:
                    if len(stack[str(event.pitch)+str(event.channel)]) > 0:  ### MODIFIED TO CONDITIONALLY POP ###
                        stack[str(event.pitch)+str(event.channel)].pop()
                    tempEventList.append(event)
```

You will also need to install fluidsynth. `sudo apt-get install fluidsynth` should do. 

You also need to find a soundfont. There's a bunch of free ones online, but try to get a GM soundfont so that percussion will work properly. 
