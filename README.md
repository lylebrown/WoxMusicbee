# WoxMusicbee
Musicbee plugin for the Wox Launcher. Add and play tracks in Musicbee from Wox!

![Screenshot of Wox Musicbee](https://raw.githubusercontent.com/lylebrown/WoxMusicbee/master/Screenshot.png)

# Install Guide

Install the [MusicbeeIPC](http://getmusicbee.com/forum/index.php?topic=11492.0) Python SDK in the Wox Python installation. Add the MusicbeeIPC plugin to Musicbee. (Both have been tested at version 2.0.) Copy all files to the Wox plugin directory within a subfolder. Ensure Musicbee is running when using the plugin or there will be no results.

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
