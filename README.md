# WoxMusicbee
[Musicbee](http://getmusicbee.com/) plugin for the [Wox Launcher](https://www.getwox.com/). Add and play tracks in Musicbee from Wox!

![Screenshot of Wox Musicbee](https://raw.githubusercontent.com/lylebrown/WoxMusicbee/master/Screenshot.png)

# Install Guide

Install the [MusicbeeIPC](http://getmusicbee.com/forum/index.php?topic=11492.0) Python SDK in the Wox Python installation. Add the MusicbeeIPC plugin to Musicbee (both have been tested at version 2.0). [Install PyWin32](http://stackoverflow.com/a/31348620) into the Wox Python installation. Copy all files to the Wox plugin directory within a subfolder. Ensure Musicbee is running when using the plugin or there will be no results.

# Usage

    mb <command> <attribute> <keyword(s)>

Example:

    mb play track hello world

## Command words
- Play: Play the selected track immediately
- Add (or queue): Queue the selected track to play next
- Shuffle (or random): Clear playlist and shuffle entire library (no attributes)

## Attribute words
At this point in time, all attributes return tracks. In future releases [(check the beta branch!)](/tree/beta), Artist may return artist results and queue all songs by that artist, etc.

- Title (or song, or track): Searches in the title field
- Artist (or band, or singer): Searches in the Song Artist field
- Album (or cd, or record): Searches in the Album field
