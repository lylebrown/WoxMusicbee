# WoxMusicbee
Musicbee plugin for the Wox Launcher. Add and play tracks in Musicbee from Wox!

![Screenshot of Wox Musicbee](https://raw.githubusercontent.com/lylebrown/WoxMusicbee/master/Screenshot.png)

# Install Guide

Install MusicbeeIPC in the Wox Python installation. Ensure Musicbee is running when using the plugin or there will be no results.

# Usage

    mb <command> <attribute> <keyword(s)>

Example:

    mb play track hello world

## Command words
- Play: Play the selected track immediately
- Add: Queue the selected track to play next

## Attribute words
At this point in time, all attributes return tracks. In future releases, Artist may return artist results and queue all songs by that artist, etc.

- Title (or song, or track): Searches in the title field
- Artist (or band, or singer): Searches in the Song Artist field
- Album (or cd): Searches in the Album field
