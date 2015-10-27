import urllib,urllib2,re,base64,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os
import urlresolver
from t0mm0.common.addon import Addon
from t0mm0.common.net import Net
CAT = base64.decodestring('LnBocA==')
BASE = base64.decodestring('aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vaXB0di8=')
BASE2 = base64.decodestring('aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL2tpZHMv')
BASE3 = base64.decodestring('aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL3BvcC8=')
addon_id='plugin.video.GenieTv_Streams'
art = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + '/resources/art/'))
art2 =  base64.decodestring('aHR0cDovL2FyY2hpdGVjdHMueDEwaG9zdC5jb20vdm9kL2FydC8=')
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
net = Net()

def CATEGORIES():
        addDir('LIVE TV',BASE,4,art+'livetv.png')
        addDir('VIDEO ON DEMAND',BASE,5,art+'vod.png')
        
def LIVECATS():
        addDir('ENTERTAINMENT',BASE+'entertainment'+CAT,3,art+'ent.png')
        addDir('MOVIES',BASE+'movies'+CAT,3,art+'movies.png')
        addDir('SPORTS',BASE+'sports'+CAT,3,art+'sports.png')
        addDir('KIDS',BASE+'kids'+CAT,3,art+'kids.png')
        addDir('DOCUMENTARIES',BASE+'documentaries'+CAT,3,art+'docu.png')
        addDir('NEWS',BASE+'news'+CAT,3,art+'news.png')
        addDir('MUSIC CHANNELS',BASE+'music'+CAT,3,art+'music.png')
        addDir('XXX',BASE+'xxx'+CAT,3,art+'xxx.png')
        addDir('USA LIVE TV',BASE+'usatv'+CAT,3,art+'usa.png')
        addDir('LIVE EVENTS',BASE+'liveevents'+CAT,3,art+'live.png')
        
def VODCATS():
        addDir('MOVIES',BASE,7,art+'MOVIESv.png')
        addDir('POPULAR',BASE,7,art+'POPULARv.png')
        addDir('TV SHOWS',BASE,7,art+'TVSHOWSv.png')
        addDir('KIDS',BASE,6,art+'KIDSv.png')
        addDir('COMEDY',BASE,7,art+'COMEDYv.png')
      
def KIDS():
        addDir('PEPPA PIG',BASE2+'peppa'+CAT,3,'http://goo.gl/p9pakK')
		
def POP():
        addDir('FEAR THE WALKING DEAD',BASE3+'fear'+CAT,3,'http://goo.gl/ggsJ8F')

        
def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent' , "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0")
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link

def Live(url):
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_TITLE )
        vidlocation=('%s%s'%(BASE,url))
        link = OPEN_URL(url)
        match=re.compile('<a.href="(.+?)".target="_blank"><img.src="(.+?)".style="max-width:200px;"./></a><br><b>(.+?)</b>').findall(link)
        for url,iconimage,name in match:
                addDir2('%s'%(name).replace('GenieTv','[COLOR green]GenieTV[/COLOR]').replace('.',' ').replace('mp4','').replace('mkv','').replace('_',' '),'%s'%(url),2,'%s'%(iconimage))
def RESOLVE(url): 
    play=xbmc.Player(GetPlayerCore())
    import urlresolver
    try: play.play(url)
    except: pass
    from urlresolver import common
    dp = xbmcgui.DialogProgress()
    dp.create('[COLORlime]Architects@Work[/COLOR]','Opening %s Now'%(name))
    dp.update(10)
    xbmc.sleep(1000)
    dp.update(20)
    xbmc.sleep(1000)
    dp.update(30)
    xbmc.sleep(1000)
    dp.update(40)
    xbmc.sleep(1000)
    dp.update(50)
    play=xbmc.Player(GetPlayerCore())
    dp.update(60)
    url=urlresolver.HostedMediaFile(url).resolve() 
    dp.update(75)
    xbmc.sleep(1000)
    dp.update(85)
    if dp.iscanceled(): 
        print "[COLORred]STREAM CANCELLED[/COLOR]" # need to get this part working    
        dp.update(100)
        dp.close()
        dialog = xbmcgui.Dialog()
        if dialog.yesno("[B]CANCELLED[/B]", '[B]Was There A Problem[/B]','', "",'Yes','No'):
            dialog.ok("Message Send", "Your Message Has Been Sent")
        else:
	         return
    else:
        dp.update(90)
        xbmc.sleep(1000)
        dp.update(100)
        try: play.play(url)
        except: pass
        try: ADDON.resolve_url(url) 
        except: pass 
        dp.close()
       

                
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

def GetPlayerCore(): 
    try: 
        PlayerMethod=getSet("core-player") 
        if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER 
        elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER 
        elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER 
        else: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    except: PlayerMeth=xbmc.PLAYER_CORE_AUTO 
    return PlayerMeth 
    return True 
	  
def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
def addDir2(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok
        
              
params=get_params()
url=None
name=None
iconimage=None
mode=None
description=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==2:
        RESOLVE(url)
elif mode==3:
        Live(url)

elif mode==4:
        LIVECATS()

elif mode==5:
        VODCATS()

elif mode==6:
        KIDS()

elif mode==7:
        POP()

xbmcplugin.endOfDirectory(int(sys.argv[1]))
