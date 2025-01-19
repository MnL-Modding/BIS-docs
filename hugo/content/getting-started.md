---
title: "Getting started"
description: "Before setting off on your modding journey, it's important to know some terms—M&L jargon, if you will—as well as the basics of NDS ROM structure and modding."
weight: 1
prev: '/'
---


> [!IMPORTANT]
> Most of the content on this site is only applicable to the original NDS version of the game!
> The 3DS remake, *Mario & Luigi: Bowser's Inside Story + Bowser Jr.'s Journey,* is much less understood,
> but will hopefully be documented soon enough.

Before setting off on your modding journey, it's important to know
some terms---*M&L* jargon, if you will---as well as the basics of NDS ROM structure and modding.
Most tools support all region ROMs of the game.


## Terms
* **Script, scripting, scripting language, AI:** The *Mario & Luigi* games up until *Brothership* utilize a custom scripting system/language.
  It is always stored as binary, but can be recognized by its abundance of blocks of `00 00 00 00` bytes and
  other small little-endian 32-bit values (the command parameter variables bitfield).
  Although the language itself is the same, the game uses 4 different sets of commands, referred to as *dialects,*
  used in different contexts. Commands `0x0000`--`0x0046` (incl.) are the same for all dialects.
  The Battle, Menu and Shop scripts are internally referred to as *AIs* in the game's filenames (`BAI`, `MAI`, `SAI`),
  code (`clBtlAIBase`, `clMenuAIBase`, `clShopAIBase`), and footer notes.
    * **`FEvent` script, Field Event script:** This dialect is used for all scripts in the overworld.
      All of its scripts are stored in `FEvent/FEvent.dat`, which also includes the messages (dialogue) used by these scripts,
      as well as data for things like the actors in every room.
    * **Battle script, `BAI` script:** This dialect is used for, well, everything within battles.
      Its scripts are stored in the `BAI/BAI_*.dat` files, while its messages are stored in `BAI/BMes_*.dat`.
    * **Menu script, `MAI` script:** Surprise surprise, this dialect is used for scripts in menus.
      Its scripts are stored in the `MAI/MAI_*.dat` files, while its messages are stored in `MAI/MMes_yo.dat`.
    * **Shop script, `SAI` script:** You're not going to believe this, but this dialect is used for scripts in shops.
      Its scripts are stored in `SAI/SAI_tuto_yo.dat`, while its messages are stored in `SAI/SMes_yo.dat`.

* **Command, scripting command:** Commands are the basic building blocks of scripts.
  Each command can do something lower-level like "Jump" (moves the command pointer), "Add", "Multiply",
  or higher-level like "Show Textbox", "Wait for Textbox to Close", "Load Music File", etc.
  Commands are usually referred to in hex and prefixed with the dialect they exist in:
    * **`CM_`:** Common commands (`0x0000`--`0x0046` incl.), existing in all dialects.
    * **`FE_`:** `FEvent` commands.
    * **`BA_`:** Battle (AI) commands.
    * **`MA_`:** Menu (AI) commands.
    * **`SA_`:** Shop (AI) commands.

  For example: `CM_0001`, `FE_01BA`, `BA_0077`.

* **Language table:** Language tables contain text localized in multiple languages, hence the name,
  and occasionally binary data like fonts as well. They usually end with padding.

* **Text table:** An entry in a language table, contains multiple text entries, all in the same language.

* **Notes, footer notes:** These are internal notes that the developers left behind within the footers of the scripts.
  They are in Japanese, encoded in Shift JIS. You can find an automatically-generated dump of them [here](../scripting/notes.txt)
  (currently only contains notes from `FEvent` and Battle scripts). Get your translator handy!


## Let's get modding!
Depending on what you want to mod, you're going to need different tools.

### Scripts & Text
> [!CAUTION]
> As script editing tools are not all that advanced yet, you will likely have to manually mess around with
> alignment, padding, jump offsets and other stuff in order for your scripts to not crash!
> This applies even if you're only editing text. **Here be dragons!**

Most beginners are going to have an easier time with [QtMnL](https://github.com/MnL-Modding/QtMnL).
It is a GUI editor that supports editing the ROM directly.

[`mnlscript.py`](https://github.com/MnL-Modding/mnlscript.py) is a more powerful but complicated tool
that converts the *M&L* scripting language into Python and back. Although that may sound intimidating,
it can very well be easier to use than QtMnL due to its support for and inclusion of utility functions like
`wait`, `say`, and `show_save_dialog`. It is also the tool recommended for larger mods due to its
Git-friendliness, support for comments, variables, etc.

### Graphics
[Spritoglobin](https://github.com/MnL-Modding/Spritoglobin) is a tool that allows you to view sprites,
with editing support being worked on. It currently only supports the US and EU versions.

### Maps
A [Tiled](https://www.mapeditor.org) plugin for editing maps is currently being worked on.

### Audio
The game's audio, like music and sound effects, is stored in `Sound/sound_data.sdat`.
This is probably the *one* format used by the game that isn't specific to the *M&L* series, so you don't need any specialized tools
to edit it. You can use established ones like [Nitro Studio 2 (Deluxe)](https://www.romhacking.net/utilities/1639/).


## Distributing your work
So you've worked hard on you mod, and it's finally finished! Or at least, finished enough
for an alpha version you want people to check out. So you just upload the entire ROM, right?

> [!CAUTION]
> Uploading the entire ROM is illegal, even if it's modded! Instead, distribute a patch file.

So how do you create a patch file, you ask? Well, one format you can use is [Xdelta3](https://github.com/jmacd/xdelta).
Although the official program is CLI-only, there are many GUI tools for both creating and applying Xdelta3 patches.

Make sure to tell your users which region of the game the patch is based on as well!
Patches built from a given version can **only** be applied to that version.
