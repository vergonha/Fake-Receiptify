
# Fake Receiptify 👁👄👁
Instead of using your most listed songs, you can now use your favorite playlist with your favorite songs to generate a Receipt on Receiptify. 

## How to use? 🤔
1 - Login in [Receiptify](https://receiptify.herokuapp.com/) with your Spotify Account. 
![](https://imgur.com/OkvAp7P.png)

2 - Copy URL in your browser.
![](https://imgur.com/41HyIn0.png)

3 - Copy Link of your Spotify Playlist.
![](https://imgur.com/DNnm4ye.png)

4 - Open *main.py* and fill with links
![](https://imgur.com/aim9X54.png)

5 - Copy result (magenta color text)
![](https://imgur.com/6IwNuKh.png)

6 - Paste in your Browser Console
![](https://imgur.com/9h9UnLY.png)

## Attention! ⚠️

We don't storage your information, we use the Bearer Token, found in URL query "accessToken" to make requests to Spotify API.

Be careful with codes you write in Console Browser tab, most of them can be harmful or dangerous to you, we use "displayReceipt" function, a native function written Receiptify [source code](https://github.com/michellexliu/receiptify).