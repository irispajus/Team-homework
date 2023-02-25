 nums = [2,7,11,15]
    target = 26
        for ( int arv = 0; arv < nums.size(); arv++){
            for (int arv1 =0; arv1 < nums.size(); arv1++){
                if (arv != arv1){
                    if(nums[arv] + nums[arv1] == target) return {arv, arv1};
                }
            }
        }
    return{};