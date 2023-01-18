def moos(suured_kappid, väikesed_kappid, kogus):
    suured_kappe_vaja = kogus // 5
    
    if suured_kappe_vaja <= suured_kappid:
        väikesed_kappe_vaja = kogus - suured_kappe_vaja * 5
        if väikesed_kappe_vaja > väikesed_kappid:
            return -1
        else:
            return suured_kappe_vaja + väikesed_kappe_vaja
        
    elif suured_kappe_vaja > suured_kappid:
        väikesed_kappe_vaja = kogus - suured_kappid * 5
        if väikesed_kappe_vaja > väikesed_kappid:
            return -1
        else:
            return suured_kappid + väikesed_kappe_vaja
    
    else:
        return -1
    
