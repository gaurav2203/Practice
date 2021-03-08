import os
os.system("fdisk -l")
part_new= input("Enter the new partition for pv: ")
vg_name= input("Enter the name of your vg: ")
lv_name= input("Enter the name of your lv: ")
lv_size= input("Enter the size of your lv: ")

def create_lvm():
    os.system("fdisk "+part)
    os.system("pvcreate "+part_new)
    os.system("vgcreate "+vg_name+" "+part_new)
    os.system("lvcreate --size "+lv_size+"G --name "+lv_name+" "+vg_name)
    os.system("lvdisplay "+vg_name+"/"+lv_name)
    os.system("mkfs.ext4 /dev/"+vg_name+"/"+lv_name)

print("-----------------LVM PY SCRIPT----------------")
print()
print("Press1: To create a LVM")
print("Press2: To view the Physical Volume")
print("Press3: To view the Volume Group")
print("Press4: To view the Logical Volume")
print("Press5: To extend the pre-created Logical Volume")
print("Press6: To create a dir and mount the LVM")
print("Press7: To exit")
a= input("Enter your choice: ")
while(True):
    if( int(a) == 1):
        create_lvm()
        break
    elif(int(a) ==2):
         os.system("pvdisplay "+part_new)
         break
    elif(int(a) ==3):
            os.system("vgdisplay "+vg_name)
            break
    elif(int(a) ==4):
        os.system("lvdisplay /dev/"+vg_name+"/"+lv_name)
        break
    elif(int(a) ==5):
        size= input("Enter the size: ")
        os.system("lvextend --size +"+size+"G /dev/"+vg_name+"/"+lv_name)
        os.system("resize2fs /dev/"+vg_name+"/"+lv_name)
        break
    elif(int(a) ==6):
        direc= input("Enter the dir: ")
        os.display("mkdir "+direc)
        os.display("mount /dev/"+vg_name+"/"+lv_name+" "+direc)
        break
    elif(int(a)== 7):
        break
 