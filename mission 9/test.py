import mission9



def make_test(condition):
    if condition:
        print("test ok")
    else:
        print("test failed")
        
        
duree = Duree(0, 1, 0)
expected_seconds = 60

make_test(duree.toSecondes() == expected_seconds)

expected_answer = """Album 21 (12 chansons, 00:47:11)
01: White_Wedding - Billy_Idol - 00:04:12
02: Stand_And_Deliver - Adam_&_The_Ants - 00:03:33
03: You_Spin_Me_Around - Dead_Or_Alive - 00:03:14
04: Wired_For_Sound - Cliff_Richard - 00:03:38
05: Some_Like_It_Hot - The_Power_Station - 00:03:45
06: 99_Luftballons - Nena - 00:03:50
07: Keep_On_Loving_You - Reo_Speedwagon - 00:03:22
08: Seven_Into_The_Sea - In_Tua_Nua - 00:03:51
09: Love_Is_A_Battlefield - Pat_Benatar - 00:05:20
10: Etienne - Guesch_Patti - 00:04:07
11: This_Is_Not_A_Love_Song - Public_Image_Limited - 00:04:12
12: Love_Missile_F1-11 - Sigue_Sigue_Sputnik - 00:04:07"""

        
make_test(albums[-1] == espected_answer)

