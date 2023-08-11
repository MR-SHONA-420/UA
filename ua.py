#coding/utf/
#created/by/mr.Adi
import os
import random
def clear():
    os.system('clear')
    print(logo)
logo=("""   \x1b[1;97m 
 ######  ##     ##  #######  ##    ##    ###    
##    ## ##     ## ##     ## ###   ##   ## ##   
##       ##     ## ##     ## ####  ##  ##   ##  
 ######  ######### ##     ## ## ## ## ##     ## 
      ## ##     ## ##     ## ##  #### ######### 
##    ## ##     ## ##     ## ##   ### ##     ## 
 ######  ##     ##  #######  ##    ## ##     ## 
\033[91;1m--------------------------------------------------
\033[97;1mVERSION     : ULTRA PRO MAX
\033[97;1mFACEBOOK   : M.R SHONA
\033[97;1mTOOL TYPE   : \x1b[96;1mAUTO UA MAKER
\033[91;1m--------------------------------------------------""")
clear()
print('\033[0;97m[+] \033[0;96mYOUR UA \033[97;1m[\033[93;1mUSERAGENT\033[97;1m] \033[96;1mLIST HERE\n\033[1;97m==================================================')
for i in range(100):
    version_ = str(random.randint(4, 10)) + "." + str(random.randint(0, 4)) + "." + str(random.randint(0, 4))
    model_ = "SM-" + str(random.randint(100, 999))
    brand_name_ = random.choice(["Samsung", "Kaios", "Realme", "Nokia", "infinix"])
    width_ = random.randint(320, 1080)
    height_ = random.randint(480, 1920)
    user_agent = '\033[1;97m[\033[1;96mUSERAGENT\033[1;97m] \033[1;92mDavik/2.1.0 (Linux; U; Android '+version_+'.0.0; '+model_+' Build/8BFOHT) [FBAN/FB4A;FBAV/92.866.944.616;FBPN/com.facebook.katana;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/'+brand_name_+';FBBD/'+brand_name_+';FBDV/'+brand_name_+';FBSV/'+brand_name_+'.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width='+str(width_)+',height='+str(height_)+'};]'
    print(user_agent)