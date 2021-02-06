nam_nhan(dinh_thuc).
nam_nhan(trong_nghia).
nam_nhan(thanh_long).
nam_nhan(trung_nam).
nam_nhan(luong_nhan).
nam_nhan(minh_nguyen).
nam_nhan(danh_luu).
nam_nhan(cong_minh).
nam_nhan(dai_long).
nu_nhan(trung_nhan).
nu_nhan(bui_nguyen).
nu_nhan(duc_nang).
nu_nhan(minh_quan).
nu_nhan(null).
nu_nhan(tran_nam).
nu_nhan(cao_phuc).
nu_nhan(dai_nghia).
nu_nhan(phuong_nam).
thanh_hon(trung_nam, phuc_nguyen).
thanh_hon(trong_nghia, trung_nhan).
thanh_hon(thanh_long, bui_nguyen).
thanh_hon(danh_luu, phuong_nam).
thanh_hon(cong_minh, dai_nghia).
thanh_hon(minh_nguyen, cao_phuc).
thanh_hon(dai_long, tran_nam).
thanh_hon(dinh_thuc, null).
thanh_hon(luong_nhan, duc_nang).
su_phu(trong_nghia, trung_nam).
su_phu(trong_nghia, minh_nguyen).
su_phu(trong_nghia, thanh_long).
su_phu(trong_nghia, luong_nhan).
su_phu(dinh_thuc, trong_nghia).
su_phu(minh_nguyen, dai_long).
su_phu(minh_nguyen, danh_luu).
su_phu(minh_nguyen, cong_minh).
su_to(dinh_thuc, thanh_long).
su_to(dinh_thuc, trung_nam).
su_to(dinh_thuc, luong_nhan).
su_to(dinh_thuc, danh_luu).
su_to(dinh_thuc, minh_nguyen).
su_to(dinh_thuc, cong_minh).
su_to(dinh_thuc, dai_long).
su_huynh(thanh_long, trung_nam).
su_huynh(thanh_long, minh_nguyen).
su_huynh(thanh_long, luong_nhan).
su_huynh(trung_nam, minh_nguyen).
su_huynh(trung_nam, luong_nhan).
su_huynh(minh_nguyen, luong_nhan).
su_huynh(dai_long, danh_luu).
su_huynh(dai_long, cong_minh).
su_huynh(danh_luu, cong_minh).
nuong_tu(P1, P2) :- thanh_hon(P2, P1).
tuong_cong(P1, P2) :- thanh_hon(P1, P2).
su_mau(P1, P2):- nuong_tu(P1, P3), su_phu(P3, P2).
su_de(P1, P2):- su_huynh(P2, P1).
tau_tau(P1, P2):- nuong_tu(P1, P3), su_de(P2, P3).
de_muoi(P1, P2):- nuong_tu(P1, P3), su_de(P3, P2).
su_ba(P1, P2):- su_huynh(P1, P3), su_phu(P3, P2).
su_thuc(P1, P2):- su_de(P1, P3), su_phu(P3, P2).
su_nuong(P1, P2) :- nuong_tu(P1, P3), (su_ba(P3, P2); su_thuc(P3, P2)).
to_su_ba(P1, P2):- nuong_tu(P1, P3), su_to(P3, P2).










