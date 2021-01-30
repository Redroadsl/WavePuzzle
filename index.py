import wave
import os

class Media(object):
    '''Media()_VoiceMaker_Class'''
    def __init__(self):
        '''__init__()_InitialFunction.'''
        self.o=False
        self.file=r"./output.wav"
        self.lib=r"./lib/"
        self.ld={}
        self.params = [ 1, 2, 44100, 32768, 'NONE', None ]
        #params=nchannels, sampwidth, framerate,nframes, comptype, compname
    def param(self,nchannels=1,sampwidth=4,framerate=24000,nframes=8192,comptype='NONE',compname=None):
        '''param(self,nchannels=1,sampwidth=4,framerate=24000,nframes=8192,comptype='NONE',compname=None)_set params.'''
        self.params=[nchannels,sampwidth,framerate,nframes,comptype,compname]
        if self.o:
            self.wav.setparams(self.params)
    def openfile(self):
        self.wav=wave.open(self.file,mode='wb')
        self.wav.setparams(self.params)
        self.o=True
    def closefile(self):
        if self.o:
            self.wav.close()
            self.o=False
    def make(self,ci=[{'pitch':24000,'ci':'a','len':128},{'pitch':30000,'ci':'e','len':128},{'pitch':24000,'ci':'yi','len':128}]):
        self.cis=[]
        for note in ci:
            if not note.get('ci') in self.cis:
                self.cis.append(note.get('ci'))#预加载歌词
        #print(ci)
        #print(self.cis)
        for l in self.cis:#预加载声库
            self.i={'ld':None}
            self.temp_f='{}{}.wav'.format(self.lib,l)
            self.temp=wave.open(self.temp_f)
            self.temp_p=self.temp.getparams()
            self.i['ld']=self.temp.readframes(self.temp_p[3])
            self.ld[l]=self.i
            self.temp.close()
        #print(self.ld)
        for note in ci:
##            for l in range(note.get('len')):
##                #self.param(framerate=note['pitch'])
##                self.wav.writeframes(self.ld[note.get('ci')].get('ld'))
            self.wav.writeframes(self.ld[note.get('ci')].get('ld'))#run once((2.0))
            print(note)

if __name__=='__main__':
    media=Media()
    media.openfile()
    c=input('CI')#and Len
    clist=[]
    c=c.split(',')
    ##for x in range(0,len(c),2):
    ##    clist.append({'ci':c[x],'len':int(c[x+1])})
    for x in range(0,len(c),1):
        clist.append({'ci':c[x],'len':1})
    media.make(clist)
    media.closefile()
    os.system(r"output.wav")
#读取音频，字符串格式
#getBytelike this:  b'00112233' formarted: b'abcd'
#waveData = np.fromstring(strData,dtype=np.int16)#将字符串转化为int
#waveData = waveData*1.0/(max(abs(waveData)))#wave幅值归一化

