# -*- coding: utf-8 -*-
import ARIFISTIFIK
from ARIFISTIFIK import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
import youtube_dl

arif = LineClient()
#arif = LineClient(id='EMAILMU', passwd='PASSWORDMU')
#arif = LineClient(authToken='') 
arif.log("Auth Token : " + str(arif.authToken))
#========================================================
channel = LineChannel(arif)
arif.log("Channel Access Token : " + str(channel.channelAccessToken))
#========================================================
arifProfile = arif.getProfile()
arifSettings = arif.getSettings()
arifPoll = LinePoll(arif)
arifMID = arif.profile.mid
#call = LineCall(arif)

contact = arif.getProfile()
backup = arif.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus
#====================================

helpMessage ="""╭━ W✒ E━ L✒ C━ O✒ M━ E✒✒✒
╰╮┏━┳┳┳┓  ┏┳┳┳┳┳┓  ┏┳┳┳┳┳┓
┏┻╋━╋┻┻┫  ┣┻┻┻┻┻┫  ┣┻┻┻┻┻┫
┃ARIF_MH ◾◾┃ ◾ JANGAN TYPO. ▪┃
┣ⓞ━━━ⓞ┻━┻ⓞ━━ⓞ┻━┻ⓞ━━ⓞ╯
┣✠━━─「 Myhelp」
┣✠━━─「 Me」
┣✠━━─「 Mymid」
┣✠━━─「 Myname」
┣✠━━─「 Mybio」
┣✠━━─「 Mypicture」
┣✠━━─「 Myvideoprofile」
┣✠━━─「 Mycover」
┣✠━━─「 Stealprofile「@」
┣✠━━─「 Unsend me」
┣✠━━─「 Getsq」
┣✠━━─「 Lc 「@」
┣✠━━─「 Gc 「@」
┣✠━━─「 Sticker: 「angka」
┣✠━━─「 Yt: 「text」
┣✠━━─「 Image: 「text」
┣✠━━─「 Gcreator」
┣✠━━─「 Say: text」
┣✠━━─「 Apakah text」
┣✠━━─「 SearchMusic 」
┣✠━━─「 Sytr: text」
┣✠━━─「 Tr: text」
┣✠━━─「 Speed」
┣✠━━─「 Spic @」
┣✠━━─「 Scover @」
┣✠━━─「 Tagall」
┣✠━━─「 Ceksider」
┣✠━━─「 Offread」
┣✠━━─「 Listgroup」
┣✠━━─「 Restart」
┣✠━━─「 Friendlist」
┣✠━━─「 Cloneprofile @」
┣✠━━─「 Restoreprofile」
┣✠━━─「 Lurking on」
┣✠━━─「 Lurking」
┣✠━━─「 lurking off」
┣✠━━─「 Lurking reset」
┣✠━━─「 kick @」
┣✠━━─「 Mode:self」
┣✠━━─「 Mode:public」
┣╔═╦═╗╔═╗╔═╦╗╔╦╗╔╗╔╗╔═╗╔╗─╔═╗
┣║║║║║║╦╝║║║║║║║║╚╝║║╦╝║║─║╬║
┣║║║║║║╩╗║║║║║║║║╔╗║║╩╗║╚╗║╔╝
┣╚╩═╩╝╚═╝╚╩═╝╚═╝╚╝╚╝╚═╝╚═╝╚╝
╰─━─━─━──━─━≪❂≫─━─━─━─━─━─━
"""

poll = LinePoll(arif)
mode='self'
cctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

settings = {
    "keyCommand": "",
    "setKey":False
}

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = arifProfile.displayName
myProfile["statusMessage"] = arifProfile.statusMessage
myProfile["pictureStatus"] = arifProfile.pictureStatus
#==========================================
#========================================
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
    
def music(songname):
    params = {'songname':songname}
    url = 'http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params)
    r = requests.get(url,verify=False).text
    data = json.loads(r)
    for song in data:
        return song[4]

def find(songname):
    params = {'songname':songname}
    url = 'http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params)
    r = requests.get(url,verify=False).text
    data = json.loads(r)
    for song in data:
        return song[4]

def findLyric(to,song):
    params = {'songname':song}
    r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?'+urllib.urlencode(params))
    data = r.text
    data = data.encode('utf-8')
    data = json.loads(data)
    for song in data:
        arif.sendText(to,"Lyrics Of " + song[0] + ":\n\n"+ song[5])
    
#=======================================
while True:
    try:
        ops=poll.singleTrace(count=50)
        if ops != None:
          for op in ops:
#=========================================================================================================================================#
            #if op.type in OpType._VALUES_TO_NAMES:
            #    print("[ {} ] {}".format(str(op.type), str(OpType._VALUES_TO_NAMES[op.type])))
#=========================================================================================================================================#
            if op.type == 25:
                msg = op.message
                text = msg.text
                cmd = msg.text
                msg_id = msg.id
                receiver = msg.to
                to = receiver
                sender = msg._from
                setKey = settings["keyCommand"].title()
                if settings["setKey"] == False:
                    setKey = ''
                try:
                    if msg.contentType == 0:
                        if msg.toType == 2:
                            arif.sendChatChecked(receiver, msg_id)
                            contact = arif.getContact(sender)            
                            if text.lower() == 'me':
                                arif.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                            elif text.lower() == 'mymid':
                                arif.sendMessage(msg.to,"[MID]\n" +  arifMID)
                            elif text.lower() == 'myname':
                                me = arif.getContact(arifMID)
                                arif.sendMessage(msg.to,"[DisplayName]\n" + me.displayName)
                            elif text.lower() == 'mybio':
                                me = arif.getContact(arifMID)
                                arif.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
                            elif text.lower() == 'mypicture':
                                me = arif.getContact(arifMID)
                                arif.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                            elif text.lower() == 'myvideoprofile':
                                me = arif.getContact(arifMID)
                                arif.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                            elif text.lower() == 'mycover':
                                me = arif.getContact(arifMID)
                                cover = channel.getProfileCoverURL(arifMID)    
                                arif.sendImageWithURL(msg.to, cover)
                            elif "stealprofile" in msg.text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = arif.getContact(ls)
                                        cu = channel.getProfileCoverURL(ls)
                                        path = str(cu)
                                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                        arif.sendMessage(msg.to,"Nama :\n" + contact.displayName + "\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage)
                                        arif.sendImageWithURL(msg.to,image)
                                        arif.sendImageWithURL(msg.to,path)
                            elif "cloneprofile" in msg.text.lower():
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    for mention in mentionees:
                                        contact = mention["M"]
                                        break
                                    try:
                                        arif.cloneContactProfile(contact)
                                        arif.sendMessage(msg.to, "Berhasil clone member tunggu beberapa saat sampai profile berubah")
                                    except:
                                        arif.sendMessage(msg.to, "Gagal clone member")
                            elif text.lower() == 'restoreprofile':
                                try:
                                    arifProfile.displayName = str(myProfile["displayName"])
                                    arifProfile.statusMessage = str(myProfile["statusMessage"])
                                    arifProfile.pictureStatus = str(myProfile["pictureStatus"])
                                    arif.updateProfileAttribute(8, arifProfile.pictureStatus)
                                    arif.updateProfile(arifProfile)
                                    arif.sendMessage(msg.to, "Berhasil restore profile tunggu beberapa saat sampai profile berubah")
                                except:
                                    arif.sendMessage(msg.to, "Gagal restore profile")
#====================================================
                            elif text.lower() == 'announce':
                                gett = arif.getChatRoomAnnouncements(receiver)
                                for a in gett:
                                    aa = arif.getContact(a.creatorMid).displayName
                                    bb = a.contents
                                    cc = bb.link
                                    textt = bb.text
                                    arif.sendText(receiver, 'Link: ' + str(cc) + '\nText: ' + str(textt) + '\nMaker: ' + str(aa))
#----------------Commandtambahan----------------------#
                            elif msg.text in ["Listgroup"]:
                               gid = arif.getGroupIdsJoined()
                               h = ""
                               for i in gid:
                                h += "[>] %s  \n" % (arif.getGroup(i).name + " | 「Members 」: " + str(len (arif.getGroup(i).members)))
                               arif.sendText(msg.to, ">>>>「Group List」<<<<\n"+ h +">>>>「Total Group」 : " +str(len(gid)))
                               
#===================================================
                            elif cmd.startswith("searchmusic "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╔━━[ Result Music ]"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n┣ {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n╚━━[ Total {} Music ]".format(str(len(data["result"])))
                                    ret_ += "\n\nUntuk Melihat Details Music, silahkan gunakan command {}SearchMusic {}|「number」".format(str(setKey), str(search))
                                    arif.sendMessage(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            ret_ = "╔━━[ Music ]"
                                            ret_ += "\n┣ Title : {}".format(str(data["result"]["song"]))
                                            ret_ += "\n┣ Album : {}".format(str(data["result"]["album"]))
                                            ret_ += "\n┣ Size : {}".format(str(data["result"]["size"]))
                                            ret_ += "\n┣ Link : {}".format(str(data["result"]["mp3"][0]))
                                            ret_ += "\n╚━━[ Finish ]"
                                            arif.sendImageWithURL(to, str(data["result"]["img"]))
                                            arif.sendMessage(to, str(ret_))
                                            arif.sendAudioWithURL(to, str(data["result"]["mp3"][0]))                               
#===================================================
                            elif text.lower() == 'unsend me':
                                arif.unsendMessage(msg_id)
                            elif text.lower() == 'getsq':
                                a = arif.getJoinedSquares()
                                squares = a.squares
                                members = a.members
                                authorities = a.authorities
                                statuses = a.statuses
                                noteStatuses = a.noteStatuses
                                txt = str(squares)+'\n\n'+str(members)+'\n\n'+str(authorities)+'\n\n'+str(statuses)+'\n\n'+str(noteStatuses)+'\n\n'
                                txt2 = ''
                                for i in range(len(squares)):
                                    txt2 += str(i+1)+'. '+str(squares[i].invitationURL)+'\n'
                                arif.sendText(receiver, txt2)
                            elif 'lc ' in text.lower():
                                try:
                                    typel = [1001,1002,1003,1004,1005,1006]
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = arif.getContact(u).mid
                                    s = arif.getContact(u).displayName
                                    hasil = channel.getHomeProfile(mid=a)
                                    st = hasil['result']['feeds']
                                    for i in range(len(st)):
                                        test = st[i]
                                        result = test['post']['postInfo']['postId']
                                        channel.like(str(sender), str(result), likeType=random.choice(typel))
                                        channel.comment(str(sender), str(result), 'Auto Like by ARIFISTIFIK\n ☬[ARIFISTIFIK]☪➣')
                                    arif.sendText(receiver, 'Done Like+Comment '+str(len(st))+' Post From' + str(s))
                                except Exception as e:
                                    arif.sendText(receiver, str(e))
                            elif 'gc ' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    cname = arif.getContact(u).displayName
                                    cmid = arif.getContact(u).mid
                                    cstatus = arif.getContact(u).statusMessage
                                    cpic = arif.getContact(u).picturePath
                                    arif.sendText(receiver, 'Nama : '+cname+'\nMID : '+cmid+'\nStatus Msg : '+cstatus+'\nPicture : http://dl.profile.line.naver.jp'+cpic)
                                    arif.sendMessage(receiver, None, contentMetadata={'mid': cmid}, contentType=13)
                                    if arif.getContact(u).videoProfile != None:
                                        arif.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic+'/vp.small')
                                    else:
                                        arif.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic)
                                except Exception as e:
                                    arif.sendText(receiver, str(e))
                            elif 'sticker:' in msg.text.lower():
                                try:
                                    query = msg.text.replace("sticker:", "")
                                    query = int(query)
                                    if type(query) == int:
                                        arif.sendImageWithURL(receiver, 'https://stickershop.line-scdn.net/stickershop/v1/product/'+str(query)+'/ANDROID/main.png')
                                        arif.sendText(receiver, 'https://line.me/S/sticker/'+str(query))
                                    else:
                                        arif.sendText(receiver, 'gunakan key sticker angka bukan huruf')
                                except Exception as e:
                                    arif.sendText(receiver, str(e))
                            elif "yt:" in msg.text.lower():
                                try:
                                    query = msg.text.replace("yt:", "")
                                    query = query.replace(" ", "+")
                                    x = arif.youtube(query)
                                    arif.sendText(receiver, x)
                                except Exception as e:
                                    arif.sendText(receiver, str(e))
                            elif "image:" in msg.text.lower():
                                try:
                                    query = msg.text.replace("image:", "")
                                    images = arif.image_search(query)
                                    arif.sendImageWithURL(receiver, images)
                                except Exception as e:
                                    arif.sendText(receiver, str(e))
                            elif 'say:' in msg.text.lower():
                                try:
                                    isi = msg.text.lower().replace('say:','')
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp.mp3')
                                    arif.sendAudio(receiver, 'temp.mp3')
                                except Exception as e:
                                    arif.sendText(receiver, str(e))
                            elif 'apakah ' in msg.text.lower():
                                try:
                                    txt = ['iya','tidak','bisa jadi']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    arif.sendAudio(receiver, 'temp2.mp3')
                                except Exception as e:
                                    arif.sendText(receiver, str(e))
                            elif "sytr:" in msg.text:
                                try:
                                    isi = msg.text.split(":")
                                    translator = Translator()
                                    hasil = translator.translate(isi[2], dest=isi[1])
                                    A = hasil.text
                                    tts = gTTS(text=A, lang=isi[1], slow=False)
                                    tts.save('temp3.mp3')
                                    arif.sendAudio(receiver, 'temp3.mp3')
                                except Exception as e:
                                    arif.sendText(receiver, str(e))
#============================================================#HELPSTART#=========================================================#
                            elif text.lower() == 'myhelp':
                                arif.sendText(msg.to,helpMessage)
                                print ("[COMMAND] HELP")
                                
                                
                            elif text.startswith("imagetext "):
                                sep = text.split(" ")
                                textnya = text.replace(sep[0] + " ","")   
                                urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                                arif.sendImageWithURL(msg.to, urlnya)   
                                
                            elif text.startswith("musik "):
                                try:
                                    sep = msg.text.split(" ")
                                    songname = msg.text.replace(sep[0] + " ","")
                                    params = {'songname': songname}
                                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.parse.urlencode(params))
                                    data = r.text
                                    data = json.loads(data)
                                    for song in data:
                                        hasil = 'This is Your Music\n'
                                        hasil += 'Judul : ' + song[0]
                                        hasil += '\nDurasi : ' + song[1]
                                        hasil += '\nLink Download : ' + song[4]
                                        arif.sendMessage(msg.to, hasil)
                                        arif.sendMessage(msg.to, "Please Wait for Music...")
                                        arif.sendAudioWithURL(msg.to, song[4])
                                except Exception as njer:
                                        arif.sendMessage(msg.to, str(njer))                             
#============================================================#MODE / RESTART#======================================================#
                            elif text.lower() == 'restart':
                                arif.sendText(receiver, '「Bot restart」')
                                print ("BOT RESTART")
                                restart_program()
                            elif text.lower() == 'friendlist':
                                contactlist = arif.getAllContactIds()
                                kontak = arif.getContacts(contactlist)
                                num=1
                                msgs="━━━━━━━━━List Friend━━━━━━━━━"
                                for ids in kontak:
                                    msgs+="\n[%i] %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n━━━━━━━━━List Friend━━━━━━━━━\n\nTotal Friend : %i" % len(kontak)
                                arif.sendMessage(msg.to, msgs)
#============================================================#ULTI STARTR#=========================================================#
                            elif 'kick' in text.lower():
                                   targets = []
                                   key = eval(msg.contentMetadata["MENTION"])
                                   key["MENTIONEES"] [0] ["M"]
                                   for x in key["MENTIONEES"]:
                                       targets.append(x["M"])
                                   for target in targets:
                                       try:
                                           arif.kickoutFromGroup(msg.to,[target])                           
                                       except:
                                           arif.sendText(msg.to,"Error")
#======================================================             
                            elif text == "invgroupcall":
                                if msg.toType == 2:
                                    group = arif.getGroup(to)
                                    members = [mem.mid for mem in group.members]
                                    call.acquireGroupCallRoute(to)
                                    call.inviteIntoGroupCall(to, contactIds=members)
                                    arif.sendMessage(to, "Done invite group call")                                         
#===============================================================================================================#
                            elif msg.text in ["Gcreator"]:
                              if msg.toType == 2:
                                    ginfo = arif.getGroup(msg.to)
                                    gCreator = ginfo.creator.mid
                                    try:
                                        gCreator1 = ginfo.creator.displayName

                                    except:
                                        gCreator = "Error"
                                    arif.sendMessage(receiver, None, contentMetadata={'mid': gCreator}, contentType=13)
                                    arif.sendText(msg.to, "「Group Creator」 : " + gCreator1)
                                    arif.tag(receiver, gCreator)
#===================
                            elif "tr:" in msg.text:
                                try:
                                    isi = msg.text.split(":")
                                    translator = Translator()
                                    hasil = translator.translate(isi[2], dest=isi[1])
                                    A = hasil.text                               
                                    arif.sendText(receiver, str(A))
                                except Exception as e:
                                    arif.sendText(receiver, str(e))
                            elif text.lower() == 'speed':
                                start = time.time()
                                arif.sendText(receiver, "TestSpeed")
                                elapsed_time = time.time() - start
                                arif.sendText(receiver, "%sdetik" % (elapsed_time))
                            elif 'spic' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = arif.getContact(u).pictureStatus
                                    if arif.getContact(u).videoProfile != None:
                                        arif.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a+'/vp.small')
                                    else:
                                        arif.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a)
                                except Exception as e:
                                    arif.sendText(receiver, str(e))
                            elif 'scover' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = channel.getProfileCoverURL(mid=u)
                                    arif.sendImageWithURL(receiver, a)
                                except Exception as e:
                                    arif.sendText(receiver, str(e))
                            elif text.lower() == 'tagall':
                                group = arif.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//20
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*20 : (a+1)*20]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Alin \n'
                                    arif.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                    arif.sendMessage(to, "Hello {} Mention".format(str(len(nama)))) 
                            elif text.lower() == 'ceksider':
                                try:
                                    del cctv['point'][receiver]
                                    del cctv['sidermem'][receiver]
                                    del cctv['cyduk'][receiver]
                                except:
                                    pass
                                cctv['point'][receiver] = msg.id
                                cctv['sidermem'][receiver] = ""
                                cctv['cyduk'][receiver]=True
                            elif text.lower() == 'offread':
                                if msg.to in cctv['point']:
                                    cctv['cyduk'][receiver]=False
                                    arif.sendText(receiver, cctv['sidermem'][msg.to])
                                else:
                                    arif.sendText(receiver, "Heh belom di Set")
                            elif text.lower() == 'mode:self':
                                mode = 'self'
                                arif.sendText(receiver, 'Mode Public Off')
                            elif text.lower() == 'mode:public':
                                mode = 'public'
                                arif.sendText(receiver, 'Mode Public ON')
                            elif text.lower() == 'restart':
                                restart_program()
                      #                LOOK SIDER                  #                    
                            elif text.lower() == 'lurking on':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in read['readPoint']:
                                        try:
                                            del read['readPoint'][msg.to]
                                            del read['readMember'][msg.to]
                                            del read['readTime'][msg.to]
                                        except:
                                            pass
                                        read['readPoint'][msg.to] = msg.id
                                        read['readMember'][msg.to] = ""
                                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                        read['ROM'][msg.to] = {}
                                        with open('sider.json', 'w') as fp:
                                            json.dump(read, fp, sort_keys=True, indent=4)
                                            arif.sendMessage(msg.to,"Lurking already on")
                                else:
                                    try:
                                        del read['readPoint'][msg.to]
                                        del read['readMember'][msg.to]
                                        del read['readTime'][msg.to]
                                    except:
                                        pass
                                    read['readPoint'][msg.to] = msg.id
                                    read['readMember'][msg.to] = ""
                                    read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                    read['ROM'][msg.to] = {}
                                    with open('sider.json', 'w') as fp:
                                        json.dump(read, fp, sort_keys=True, indent=4)
                                        arif.sendMessage(msg.to, "Set reading point:\n" + readTime)
                                        
                            elif text.lower() == 'lurking off':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to not in read['readPoint']:
                                    arif.sendMessage(msg.to,"Lurking already off")
                                else:
                                    try:
                                            del read['readPoint'][msg.to]
                                            del read['readMember'][msg.to]
                                            del read['readTime'][msg.to]
                                    except:
                                          pass
                                    arif.sendMessage(msg.to, "Delete reading point:\n" + readTime)
                
                            elif text.lower() == 'lurking reset':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in read["readPoint"]:
                                    try:
                                        read["readPoint"][msg.to] = True
                                        read["readMember"][msg.to] = {}
                                        read["readTime"][msg.to] = readTime
                                        read["ROM"][msg.to] = {}
                                    except:
                                        pass
                                    arif.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                                else:
                                    arif.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                                    
                            elif text.lower() == 'lurking':
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    if read["ROM"][receiver].items() == []:
                                        arif.sendMessage(receiver,"[ Reader ]:\nNone")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = arif.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = 'Lurkers:\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@c\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\nLurking time: \n" + readTime
                                    try:
                                        arif.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    arif.sendMessage(receiver,"Lurking has not been set.")
                except Exception as e:
                    arif.log("[SEND_MESSAGE] ERROR : " + str(e))
#=========================================================================================================================================#
            elif mode == 'public' and op.type == 26:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                try:
                    if msg.contentType == 0:
                        if msg.toType == 2:
                            arif.sendChatChecked(receiver, msg_id)
                            contact = arif.getContact(sender)
                            if text.lower() == 'me':
                                arif.sendMessage(receiver, None, contentMetadata={'mid': sender}, contentType=13)
                                arif.tag(receiver, sender)
                            elif 'gc ' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    cname = arif.getContact(u).displayName
                                    cmid = arif.getContact(u).mid
                                    cstatus = arif.getContact(u).statusMessage
                                    cpic = arif.getContact(u).picturePath
                                    arif.sendText(receiver, 'Nama : '+cname+'\nMID : '+cmid+'\nStatus Msg : '+cstatus+'\nPicture : http://dl.profile.line.naver.jp'+cpic)
                                    arif.sendMessage(receiver, None, contentMetadata={'mid': cmid}, contentType=13)
                                    if arif.getContact(u).videoProfile != None:
                                        arif.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic+'/vp.small')
                                    else:
                                        arif.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp'+cpic)
                                except Exception as e:
                                    arif.sendText(receiver, str(e))                            
                            elif 'sticker:' in msg.text.lower():
                                try:
                                    query = msg.text.replace("sticker:", "")
                                    query = int(query)
                                    if type(query) == int:
                                        arif.sendImageWithURL(receiver, 'https://stickershop.line-scdn.net/stickershop/v1/product/'+str(query)+'/ANDROID/main.png')
                                        arif.sendText(receiver, 'https://line.me/S/sticker/'+str(query))
                                    else:
                                        arif.sendText(receiver, 'gunakan key sticker angka bukan huruf')
                                except Exception as e:
                                    arif.sendText(receiver, str(e))
                            elif "yt:" in msg.text.lower():
                                try:
                                    query = msg.text.replace("yt:", "")
                                    query = query.replace(" ", "+")
                                    x = arif.youtube(query)
                                    arif.sendText(receiver, x)
                                except Exception as e:
                                    arif.sendText(receiver, str(e))
                            elif "image:" in msg.text.lower():
                                try:
                                    query = msg.text.replace("image:", "")
                                    images = arif.image_search(query)
                                    arif.sendImageWithURL(receiver, images)
                                except Exception as e:
                                    arif.sendText(receiver, str(e))
                            elif 'say:' in msg.text.lower():
                                try:
                                    isi = msg.text.lower().replace('say:','')
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp.mp3')
                                    arif.sendAudio(receiver, 'temp.mp3')
                                except Exception as e:
                                    arif.sendText(receiver, str(e))
                            elif 'apakah ' in msg.text.lower():
                                try:
                                    txt = ['iya','tidak','bisa jadi']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    arif.sendAudio(receiver, 'temp2.mp3')
                                except Exception as e:
                                    arif.sendText(receiver, str(e))
                            elif "sytr:" in msg.text:
                                try:
                                    isi = msg.text.split(":")
                                    translator = Translator()
                                    hasil = translator.translate(isi[2], dest=isi[1])
                                    A = hasil.text
                                    tts = gTTS(text=A, lang=isi[1], slow=False)
                                    tts.save('temp3.mp3')
                                    arif.sendAudio(receiver, 'temp3.mp3')
                                except Exception as e:
                                    arif.sendText(receiver, str(e))
                            elif "tr:" in msg.text:
                                try:
                                    isi = msg.text.split(":")
                                    translator = Translator()
                                    hasil = translator.translate(isi[2], dest=isi[1])
                                    A = hasil.text                               
                                    arif.sendText(receiver, str(A))
                                except Exception as e:
                                    arif.sendText(receiver, str(e))
                            elif text.lower() == 'speed':
                                start = time.time()
                                arif.sendText(receiver, "TestSpeed")
                                elapsed_time = time.time() - start
                                arif.sendText(receiver, "%sdetik" % (elapsed_time))
                            elif 'spic' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = arif.getContact(u).pictureStatus
                                    if arif.getContact(u).videoProfile != None:
                                        arif.sendVideoWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a+'/vp.small')
                                    else:
                                        arif.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a)
                                except Exception as e:
                                    arif.sendText(receiver, str(e))
                            elif 'scover' in text.lower():
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = channel.getProfileCoverURL(mid=u)
                                    arif.sendImageWithURL(receiver, a)
                                except Exception as e:
                                    arif.sendText(receiver, str(e))
                except Exception as e:
                    arif.log("[SEND_MESSAGE] ERROR : " + str(e))
#=========================================================================================================================================#
            if op.type == 55:
                print ("[ 55 ] NOTIFIED READ MESSAGE")
                try:
                    if op.param1 in read['readPoint']:
                        if op.param2 in read['readMember'][op.param1]:
                            pass
                        else:
                            read['readMember'][op.param1] += op.param2
                        read['ROM'][op.param1][op.param2] = op.param2
                    else:
                       pass
                except:
                    pass         

            elif op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = arif.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n~ " + Name
                                pref=['eh ada','hai kak','aloo..','nah','lg ngapain','halo','sini kak']
                                arif.sendText(op.param1, str(random.choice(pref))+' '+Name)
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

            else:
                pass
#=========================================================================================================================================#
            # Don't remove this line, if you wan't get error soon!
            poll.setRevision(op.revision)
            
    except Exception as e:
        arif.log("[SINGLE_TRACE] ERROR : " + str(e))
