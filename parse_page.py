
import sys
import binascii
from struct import *

# typedef struct PageHeaderData
# {
# 	/* XXX LSN is member of *any* block, not only page-organized ones */
# 	PageXLogRecPtr pd_lsn;		/* LSN: next byte after last byte of xlog
# 								 * record for last change to this page */
# 	uint16		pd_checksum;	/* checksum */
# 	uint16		pd_flags;		/* flag bits, see below */
# 	LocationIndex pd_lower;		/* offset to start of free space */
# 	LocationIndex pd_upper;		/* offset to end of free space */
# 	LocationIndex pd_special;	/* offset to start of special space */
# 	uint16		pd_pagesize_version;
# 	TransactionId pd_prune_xid; /* oldest prunable XID, or zero if none */
# 	ItemIdData	pd_linp[FLEXIBLE_ARRAY_MEMBER]; /* line pointer array */
# } PageHeaderData;


file = open("/Users/luyongqiang8/workbench/1github/pg/12/data/base/16421/16425","rb")
input = file.read()
file.close()

print("数据前16字节内容:"+str(input[0:16]))




def  convertVariable(name,index,size):
    print("\n解析字段:"+name)

    temp = input[index:index+size].hex()
    value = int(temp,16).to_bytes(size,'little').hex()
    print(name+":"+value+"("+str(int(value,16))+")")
    index += size

# offset = 0
## xlogid
# temp = input[offset:4].hex()
# xlogid = int(temp,16).to_bytes(4,"little").hex()
# print("xlogid:"+xlogid)
index = 0
size = 4
convertVariable("xlogid",index,size)
index+=size

size = 4
convertVariable("xrecoff",index,size)
index+=size

size = 2
convertVariable("pd_checksum",index,size)
index+=size

size = 2
convertVariable("pd_flags",index,size)
index+=size

size = 2
convertVariable("pd_lower",index,size)
index+=size

size = 2
convertVariable("pd_upper",index,size)
index+=size


size = 2
convertVariable("pd_special",index,size)
index+=size


size = 2
convertVariable("pd_pagesize_version",index,size)
index+=size


size = 2
convertVariable("pd_prune_xid",index,size)
index+=size
