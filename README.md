# Discord CDN Downloader
Python script for downloading a text file with Discord CDN URLs.

Please note that this was originally made for downloading voice messages off of Discord.

Despite this, any type of CDN can be downloaded (provided you know what to change in the code).



## Instructions
1. Check your URL format:
   
   > I personally used Discord's developer tools (app only, CTRL+SHIFT+I) and scraped the HTML code from it, then extracted the voice message URLs from the whole code.
   >
   > If you didn't follow this method, you're on your own, sadly.
   >
   > If you did follow tihs method, you should get a URL with something like the following format:
   >
   > https://cdn.discordapp.com/attachments/{channelID}/{unknownID1}/voice-message.ogg?ex={unknownID2}&amp;is={unknownID3}&amp;hm={unknownID4}&amp;
   >
   > If not, keep looking. You can also CTRL+F "voice-message.ogg" to instantly find the URL for voice messages.

2. Check your .txt file format:

   > Each url must be on its own line
   > 
   > That's basically it



## Additional key points
1. HTML-escaped ampersands

   - You don't need to replace the HTML-escaped ampersands ("&amp;") with real ones ("&").
   - The code should sanitize the file for you.

2. 403 Errors/User-Agents

   - Some CDNs, including Discord's, occasionally reject reqeusts without a User-Agent.
   - If this happens (i.e. you see 403 errors), add the following code:
     ```
     headers = {"User-Agent": "Mozilla/5.0"}
     response = requests.get(url, stream=True, headers=headers)
     ```
   - This didn't happen to me, but just in case, it's there.

3. "Where are the files saved?"

   - All the files are going to be saved in the same directory as the python folder.
   - Make sure you pick one that you don't mind having tons of files being saved to.
