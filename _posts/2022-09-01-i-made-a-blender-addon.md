---
layout: post
title:  "I made a blender addon!"
date:   2022-09-01 22:57:41 +0100
categories: post test blog blender 3d
---
# Introduction
Uhh, so welcome to my blog! It took me a long while, but this is going to be my first real post here and I **really** don't know how to write these, so it's probably going to be a little chaotic. I hope you don't mind that, and the weird, bad, edgy header titles or whatever they're called! Also, english isn't my first language so please ignore any stupid mistakes I make! 
<sub><sup>it most likely doesn't even matter, nobody reads these nowadays. it's all videos now, or it's just me being a boomer at 22 years old lol</sup>

<br>


## A little rant
Have you ever wondered why people don't use actual level editors nowadays? You know, the ones with snapping to grids, easy texture alignment and all that. I mean, there are probably tons of small, dedicated communities for every existing editor out there, or maybe even some actual studios using their own tools, but it's not like they're as mainstream as they used to be. If not - don't worry, I can't blame you for that, because they're almost extinct. Anyway, I definitely did wonder, and I noticed that people stopped being caring about everything sticking out of bounds and stuff like that in their levels. They just use modular sets and all that, which to me is simply boring. I get that it's easier, but where's all the fun in that? I can also understand that you can get really creative with them in all kinds of ways, but more often than not it all comes down to the same thing - laziness. Okay, enough of that little rant of mine, let's get to the point.


![hammerscreen](/assets/images/Hammer_screen.jpg)
<center>Here's something I kind of grew up with - Valve Hammer Editor. This is what I mean by saying "level editor".</center>
<br>


## Blender and the endless wait for a level design addon
For the past few years I've been waiting for somebody to finally make a set of tools for blender that would turn it into an actual level creation software. Unfortunately, such thing never happened, as you yourself could probably notice. I thought that with my not-so-recent dip into Godot and its GDScript, I would be able to overcome my fear of actual programming languages and start something myself. "Why not start with the level thingy I had in mind for so long?" - I thought to myself. And so, with a cup of hot green tea on my desk, I started looking into blender addons and how they're made. And oh boy, I definitely wasn't ready for what came next.


![tutorials](/assets/images/blender-ytaddontutorial.png)
<center>There were only two people that actually made good free tutorials, yet even they didn't explain some of the stuff I needed. Here's one of them. The other one disappeared from my browsing history unfortunately. :(</center>
<br>


## A personal(?) hell called Blender addon development
So. You'd probably think that it's just regular python, it can't be that hard, right? Fuck no, you also have to learn and look the blender stuff - class registration, unregistration, types, keymaps, context and all that weird stuff. It all quickly became way too much for me to get a hold of properly. I can already imagine anyone who's reading this thinking - "B-but you're just dumb, it's all obvious! How can you not understand such simple things!?" - I agree, I might be actually smoothbrained, but I seriously think that the whole thing is incredibly convoluted, messy and hard to understand. Even the wiki doesn't provide enough documentation, and comparing it to Godot's - it's like night and day, Blender's being shit of course. Anyway, I thought of an actually genious idea - take somebody else's addon, open the files and see how it's done. Sure, it helped a bit, but still wasn't enough.

![codesnippet](/assets/images/addon-code-snippet.png)
<center>This is how the code looks. a little bit messy overall, but it works.</center>
<br>


## A light at the end of a tunnel
Fortunately, this is the point where other people's work comes in to save the day. Thanks to the addon files not being encrypted in any kind of way or something you're able to easily open them in any text editor you want. And obviously, that is what I did. It didn't make much sense to me at first, but after a little while I actually began to understand how this entire thing works and after a day or two of work I had an addon working inside of Blender. Not perfectly, but working at the very least. There was still one thing to do, though - keyboard shortcuts. The very thing that made me start the whole "project". Of course it was an actual reason, because I couldn't get that exact kind of shortcut working with just blender alone. I think that it's obvious already that not everything was as simple as it seemed, as always. Getting the shortcuts to work was easy, just a couple lines of code, but having the ability to change the shortcuts to your own liking? Nah, you'll have to work a little bit more for that. Again, the thing that saved me was somebody else's addon, because of course - blender's wiki doesn't provide any information on how to implement addon preferences. But finally, the addon is here, ready to use.

<center><img align="center" src="/assets/images/addon-showcase.gif"></center>
<center>A little preview of the addon!</center>
<br>


## Out of the dark
So, I've got the addon working, what now? Well, it's still not complete. I'd love to have a some kind of panel with all of my textures inside, with previews and all that, but I already know that it's going to be a total pain in the ass to code, so I'm just going to take a break. It's more than enough for me with its current features, so there's no point to improve it further, at least for now. Now, I'm obviously going to release it for any of you reading this thing, whether you made it through entirely or not, I don't really care. One thing though - not all of the code is mine, actually. I found some of it on github under the GPL license, so I think that me releasing it as my own version at the very least is fine. I'm going to put a link to it here, or just host it on the website - I don't really have a clue on how limited I am on Github Pages. Install it as is, please don't zip it or anything because it won't work if you do so. Don't pay too much attention towards the name, too. (*^.^*)

<center><a href="/assets/downloads/brenchtroom.py">Download the addon!</a></center>
<br>


# Conclusion
Anyway, this will be it for now. Again, it was my first time writing an actual blog post, let alone doing it completely in english. As I said in the beginning, it's not my first language so you might spot a mistake here and there. I'll be trying my best, though, so if you enjoyed reading this - please bear with me. I'm planning on writing these at least once a week, but I don't know how far I'll get with that. My life is really boring as I sit at my desk all day long, 7 days a week, but my head is running with thoughts all the time, so as long as I'll have an interesting topic in mind - I'll write a post about it. I think that's everything, I hope that it's the proper way to end these, lol. Thank you for reading and (hopefully) see you next time! (^-^*)/
