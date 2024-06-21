#!/usr/bin/python3
from utility.EncodeGenerator import EncodeGen

print("Encoding Begins...")
encode_obj = EncodeGen()
encode_list_known = encode_obj.get_encodings()
#print("imgList:", encode_obj.imgList)
encode_list_known_ids = [encode_list_known, encode_obj.idList]
#print(encode_list_known_ids)
print("Encoding Complete")

# Saving encoding to pickle file
encode_obj.save_to_pickle(encode_list_known_ids)