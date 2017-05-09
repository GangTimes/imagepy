# -*- coding: utf-8 -*-
import os, IPy

class ShotcutManager:
    shotcuts = {}
    @classmethod
    def read(cls):
        if os.path.exists(os.path.join(IPy.root_dir, 'data/shotcut.cfg')):
            pkl_file = open(os.path.join(IPy.root_dir, 'data/shotcut.cfg'),'rb')
            cls.shotcuts = eval(pkl_file.readline())
            pkl_file.close()
         
    @classmethod
    def write(cls):
        pkl_file = open(os.path.join(IPy.root_dir, 'data/shotcut.cfg'), 'wb')
        pkl_file.write(str(cls.shotcuts))
        pkl_file.close()
    
    @classmethod
    def get(cls, key):
        if key in cls.shotcuts:
            return cls.shotcuts[key]
        return None
        
    @classmethod  
    def set(cls, key, value):
        cls.shotcuts[key] = value   

    @classmethod
    def rm(cls, key):
        if key in cls.shotcuts:
            cls.shotcuts.pop(key)
    
ShotcutManager.read()

if __name__ == '__main__':
    #ShotcutManager.set('c',[1,2,3])
    ShotcutManager.rm('c')
    print(ShotcutManager.shotcuts)
    ShotcutManager.write()
    