import pyrebase as FreBse
import fb_config_backup

FB_CONFIG = fb_config_backup.FB_CONFIG
s=FreBse.initialize_app(FB_CONFIG)

FBD=s.database()

D_PATH = "HA/"

def change_value(v):
    if v==0:
        FBD.child(D_PATH+'Hall').set(v)
        FBD.child(D_PATH + 'Hall Fan').set(v)
        FBD.child(D_PATH + 'B1').set(v)
        FBD.child(D_PATH + 'B1 Fan').set(v)
        FBD.child(D_PATH + 'B2').set(v)
        FBD.child(D_PATH + 'B2 Fan').set(v)
        FBD.child(D_PATH + 'B3').set(v)
        FBD.child(D_PATH + 'B3 Fan').set(v)
        DB1 = FBD.child(D_PATH + 'Hall')
        val = DB1.get()
        if val is not None:
            print(val.val())
        else:
            return
    else:
        FBD.child(D_PATH + 'Hall').set(v)
        FBD.child(D_PATH + 'Hall Fan').set(v)
        FBD.child(D_PATH + 'B1').set(v)
        FBD.child(D_PATH + 'B1 Fan').set(v)
        FBD.child(D_PATH + 'B2').set(v)
        FBD.child(D_PATH + 'B2 Fan').set(v)
        FBD.child(D_PATH + 'B3').set(v)
        FBD.child(D_PATH + 'B3 Fan').set(v)
        DB1 = FBD.child(D_PATH + 'Hall')
        val = DB1.get()
        if val is not None:
            print(val.val())
        else:
            return