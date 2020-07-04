This script will look through every .txt file in your local_files_to_trim folder and look for short sequences. It will then trim each sequence at a defined number of basepairs up and downstream.


This is useful for:

- seeing where published primers bind
- designing new primers using very long sequences that contain your gene of interest
- chopping sequences to a sensible length so you can compare them using MAFFT software


Your parameters need to be defined within the file parameters.py

- each parameter needs to be written in the same way as the example file (parameter = '')
- the length of your 'primers' (which can just be any sequence) is up to you - but longer = less likely to match every sequence and shorter = more likely to have offtarget matches. 
- There are three options for each primer, which will be worked through sequentially. When I use it, I pick multiple options around the same area to increase the chances of each sequence having a match
- If your extra basepairs up or downstream parameters end up being longer than the available sequence, it will just cut at the furthest possible point, so shorter sequences are still usable when you align them on MAFFT.


If your sequence fails (ie it cannot find a match for 1 or more primers), a blank file will be created and the terminal will let you know. It may be worth playing around with your optional primers if this is the case, and/or aligning this sequence with the others depending on its length. Unfortunately, many long sequences you are using may have been defined using shotgun sequencing, which may not always be ideal with HLA due to hyperpolymorphism. 

Sequences will be output into the same folder, but with the suffix '_trimmed.txt' added to the end. If you repeat the script, these will be replaced by new versions.