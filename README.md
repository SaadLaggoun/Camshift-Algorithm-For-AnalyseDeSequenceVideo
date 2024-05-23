A class assignement about implementing an Object tracking algorithm of choice, I've picked the Camshift algorithm.

![image](https://github.com/SaadLaggoun/Camshift-Algorithm-For-AnalyseDeSequenceVideo/assets/14249834/825a7c97-b93a-44da-ad70-d4704f6a0fc7)

This algorithm is a superset of the Meanshift algorithm. It came to light at the year of 1998 by Gary R and Bradski. The Meanshift algorithm was very limited in terms of object tracking capabilities, it struggled with rotation and orientation. That’s why the authors Gary R and Bradski created the Camshift algorithm, to supplement the Meanshift algorithm with enough functionality to surpass its problems.

I should mention that my implementation struggled some causalities, so I tried to add some tweeks so I can further improve the results *-they weren’t prefect-*, I've used mathematical morphology and tuned the parameters. But still, these tweaks were only for my problem at hand *-the video of me holding a blue book-* so you should also go through the process of trail and error to adjust my implementation to best fit your problem *-your video-*.

![image](https://github.com/SaadLaggoun/Camshift-Algorithm-For-AnalyseDeSequenceVideo/assets/14249834/7417297a-40ed-4ae9-b104-51d4825dbd67)

Have fun!
